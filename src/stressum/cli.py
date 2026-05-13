from __future__ import annotations

import argparse
import sys
from datetime import datetime
from pathlib import Path

from stressum.comparison import run_comparison
from stressum.plots import apply_paper_style


def discover_stressum_repo_root() -> Path | None:
    """Checkout root for this package, or None (e.g. wheel install)."""
    here_pkg = Path(__file__).resolve().parent
    for cur in [here_pkg, *here_pkg.parents]:
        manifest = cur / "pyproject.toml"
        if not manifest.is_file():
            continue
        try:
            text = manifest.read_text(encoding="utf-8")
        except OSError:
            continue
        if 'name = "stressum"' in text or "name = 'stressum'" in text:
            return cur
    return None


def comparison_output_dir() -> Path:
    """``<repo>/output/comparison-<timestamp>/`` or ``./output/comparison-<timestamp>/``."""
    stamp = datetime.now().strftime("%Y-%m-%d-%H%M%S-%f")
    root = discover_stressum_repo_root()
    base = (root / "output") if root is not None else Path.cwd() / "output"
    return base / f"comparison-{stamp}"


def main_compare(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Default stressum mode: compare two or more Stressar run bundles from a JSON "
            "config (HDR merge across replicas per run when logs are present)."
        ),
    )
    root = discover_stressum_repo_root()
    default_cfg = (root / "stressum-comparison.json") if root is not None else None
    parser.add_argument(
        "--config",
        type=Path,
        default=default_cfg,
        help=(
            "Path to comparison JSON (default: <repo-root>/stressum-comparison.json "
            "when running from this checkout)."
        ),
    )
    parser.add_argument(
        "--out",
        type=Path,
        default=None,
        help="Output directory (default: <repo>/output/comparison-<timestamp>/).",
    )
    parser.add_argument(
        "--no-plots",
        action="store_true",
        help="Skip PNG figure generation.",
    )
    parser.add_argument(
        "--seed",
        type=int,
        default=None,
        help="Optional RNG seed for deterministic plot styling.",
    )
    args = parser.parse_args(argv)

    if args.config is None:
        print(
            "No default config path (checkout root not detected). Pass --config /path/to.json",
            file=sys.stderr,
        )
        return 2
    cfg_path = args.config.expanduser().resolve()
    if not cfg_path.is_file():
        print(f"Comparison config not found: {cfg_path}", file=sys.stderr)
        return 2

    out = args.out.expanduser().resolve() if args.out else comparison_output_dir()
    apply_paper_style(seed=args.seed)

    code, _meta = run_comparison(cfg_path, out, no_plots=args.no_plots)
    return code


def main(argv: list[str] | None = None) -> int:
    argv = list(sys.argv[1:] if argv is None else argv)
    return main_compare(argv)


if __name__ == "__main__":
    raise SystemExit(main())
