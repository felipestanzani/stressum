"""Merge HdrHistogram logs across replica files into run-level percentiles."""

from __future__ import annotations

import sys
from dataclasses import dataclass
from pathlib import Path

from hdrh.histogram import HdrHistogram
from hdrh.log import HistogramLogReader

# Java bench typically records latency in nanoseconds (up to 60 s trackable).
_REF_HIST = HdrHistogram(1, 60_000_000_000, 5)


def _looks_like_histogram_log(path: Path) -> bool:
    try:
        head = path.read_text(encoding="utf-8", errors="strict")[:4096]
    except (OSError, UnicodeDecodeError):
        return False
    if not head.strip():
        return False
    if head.lstrip().startswith("#"):
        return True
    if "StartTimestamp" in head and "Compressed_Histogram" in head:
        return True
    # Interval lines: float,float,float,base64...
    first = head.splitlines()[0]
    return first[:1].isdigit() or first.startswith('"StartTimestamp"')


def _load_histogram_log_merged(path: Path) -> HdrHistogram | None:
    if not _looks_like_histogram_log(path):
        return None
    merged = HdrHistogram(1, 60_000_000_000, 5)
    reader = HistogramLogReader(str(path), _REF_HIST)
    try:
        while True:
            nxt = reader.add_next_interval_histogram(merged, 0.0, sys.maxsize, True)
            if nxt is None:
                break
    except (OSError, ValueError, TypeError, IndexError):
        return None
    finally:
        reader.close()
    if merged.get_total_count() == 0:
        return None
    return merged


def _infer_ns_to_ms_divisor(hist: HdrHistogram, ref_p50_ms: float | None) -> float:
    """Map raw histogram units to milliseconds using summary.json p50 as anchor."""
    raw_p50 = float(hist.get_value_at_percentile(50.0))
    if ref_p50_ms and ref_p50_ms > 0 and raw_p50 > 0:
        for div in (1.0, 1e3, 1e6):
            scaled = raw_p50 / div
            ratio = scaled / ref_p50_ms
            if 0.2 <= ratio <= 5.0:
                return div
    if raw_p50 > 500_000:
        return 1e6
    if raw_p50 > 500:
        return 1e3
    return 1.0


@dataclass(frozen=True)
class MergedLatency:
    """Run-level latency after merging HDR logs (values reported in ms)."""

    p50_ms: float
    p95_ms: float
    p99_ms: float
    p999_ms: float
    unit_divisor: float
    hdr_paths_used: tuple[str, ...]


def merge_run_histogram(
    hdr_paths: list[Path],
    *,
    ref_p50_ms: float | None,
) -> tuple[MergedLatency | None, list[str]]:
    """
    Merge all decodable histogram logs under one run into a single distribution.

    Returns (MergedLatency, warnings). On failure result is None and warnings explain why.
    """
    warnings: list[str] = []
    merged: HdrHistogram | None = None
    used: list[str] = []

    for p in sorted({x.resolve() for x in hdr_paths}):
        if not p.is_file():
            warnings.append(f"HDR path not a file: {p}")
            continue
        block = _load_histogram_log_merged(p)
        if block is None:
            warnings.append(
                f"Skipped HDR file (not a readable histogram log or empty): {p.name}"
            )
            continue
        if merged is None:
            merged = block
        else:
            try:
                merged.add(block)
            except (IndexError, ValueError) as e:
                warnings.append(f"Could not add histogram from {p.name}: {e}")
        used.append(p.as_posix())

    if merged is None or merged.get_total_count() == 0:
        return None, warnings

    div = _infer_ns_to_ms_divisor(merged, ref_p50_ms)
    if ref_p50_ms and ref_p50_ms > 0:
        raw = float(merged.get_value_at_percentile(50.0))
        if abs(raw / div - ref_p50_ms) / ref_p50_ms > 0.25:
            warnings.append(
                "Merged HDR p50 differs from summary.json median p50 by >25%; "
                "check histogram units vs summary latencyMs."
            )

    def q(pct: float) -> float:
        return float(merged.get_value_at_percentile(pct)) / div

    return (
        MergedLatency(
            p50_ms=q(50.0),
            p95_ms=q(95.0),
            p99_ms=q(99.0),
            p999_ms=q(99.9),
            unit_divisor=div,
            hdr_paths_used=tuple(used),
        ),
        warnings,
    )
