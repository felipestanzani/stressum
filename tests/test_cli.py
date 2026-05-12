from __future__ import annotations

import re
import shutil
from pathlib import Path

import pytest

from stressum.cli import default_output_dir, discover_stressum_repo_root, main

FIXTURE = Path(__file__).resolve().parent / "fixtures" / "minimal-run"

_STAMP_RE = re.compile(r"^\d{4}-\d{2}-\d{2}-\d{6}-\d{6}$")


def _single_output_session(run_copy: Path) -> Path:
    out_root = run_copy / "output"
    assert out_root.is_dir()
    children = [p for p in out_root.iterdir() if p.is_dir()]
    assert len(children) == 1
    assert _STAMP_RE.match(children[0].name)
    return children[0]


def test_cli_writes_artifacts(tmp_path: Path) -> None:
    run_copy = tmp_path / "minimal-run"
    shutil.copytree(FIXTURE, run_copy)
    code = main([str(run_copy), "--seed", "0"])
    assert code == 0
    out = _single_output_session(run_copy)
    assert (out / "narrative.md").is_file()
    assert (out / "tables.md").is_file()
    assert (out / "replica_breakdown.csv").is_file()
    assert (out / "run_summary.csv").is_file()
    assert (out / "throughput_per_replica.png").is_file()


def test_cli_no_plots(tmp_path: Path) -> None:
    run_copy = tmp_path / "minimal-run-np"
    shutil.copytree(FIXTURE, run_copy)
    code = main([str(run_copy), "--no-plots"])
    assert code == 0
    out = _single_output_session(run_copy)
    assert (out / "narrative.md").is_file()
    assert not (out / "throughput_per_replica.png").exists()


def test_batch_processes_all_run_subfolders(tmp_path: Path) -> None:
    results = tmp_path / "results"
    run_a = results / "run-a"
    run_b = results / "run-b"
    shutil.copytree(FIXTURE, run_a)
    shutil.copytree(FIXTURE, run_b)
    code = main(["batch", str(results)])
    assert code == 0
    out_a = _single_output_session(run_a)
    out_b = _single_output_session(run_b)
    assert (out_a / "narrative.md").is_file()
    assert (out_b / "narrative.md").is_file()


def test_batch_skips_empty_and_non_bundles(tmp_path: Path) -> None:
    results = tmp_path / "results"
    good = results / "z-good"
    shutil.copytree(FIXTURE, good)
    (results / "empty-dir").mkdir(parents=True)
    bad = results / "not-a-run"
    bad.mkdir()
    (bad / "readme.txt").write_text("x", encoding="utf-8")
    code = main(["batch", str(results)])
    assert code == 0
    assert _single_output_session(good)
    assert not (results / "empty-dir" / "output").exists()
    assert not (bad / "output").exists()


def test_batch_missing_results_root(tmp_path: Path) -> None:
    code = main(["batch", str(tmp_path / "does-not-exist")])
    assert code == 2


def test_batch_rejects_out() -> None:
    with pytest.raises(SystemExit) as excinfo:
        main(["batch", "--out", "/tmp"])
    assert excinfo.value.code == 2


def test_default_output_dir_uses_repo_output_when_run_inside_repo() -> None:
    root = discover_stressum_repo_root()
    assert root is not None
    run = root / "tests" / "fixtures" / "minimal-run"
    assert run.is_dir()
    out = default_output_dir(run)
    assert out.parent.parent == root / "output"
    assert out.parent.name == "minimal-run"
    assert _STAMP_RE.match(out.name)
