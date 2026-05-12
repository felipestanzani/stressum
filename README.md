# Stressar results — paper artifacts

This repository holds Stressar benchmark exports under `results/` and documentation under `stressar-docs/`. The `stressum` tool turns **one run directory** into CSV tables, Markdown summaries, and PNG figures suitable for scientific writing.

## Setup

Install [uv](https://docs.astral.sh/uv/), then:

```bash
uv sync
```

## One command per run

```bash
uv run stressum results/ojp-prod-20260512-044306
```

Artifacts are written to `<project-root>/output/<run-folder>/<YYYY-MM-dd-HHMMSS-microseconds>/` when the run path is inside this repository (otherwise `<run-dir>/output/…` if you point at a bundle outside the checkout). Override with `--out DIR` to write directly to `DIR`.

Options:

- `--out DIR` — output directory (default: project `output/<run-folder>/<timestamp>/` as above)
- `--no-plots` — skip PNG generation
- `--seed N` — RNG seed for deterministic styling where applicable

## All runs under `results/`

Process every immediate subdirectory of a folder that looks like a Stressar run bundle (each must have at least one `replica-*/summary.json`). Non-bundles are skipped with a message on standard error.

```bash
uv run stressum batch
```

This uses `./results` relative to the current working directory. To use another root:

```bash
uv run stressum batch /path/to/results
```

Each run gets its own session folder under the project `output/<run-folder>/…` (same rule as a single run: paths inside this repo use the root `output/` tree). The `--out` option is not supported in batch mode. `--no-plots` and `--seed` apply to the whole batch.

## Interpretation

See `stressar-docs/` (especially `METRICS.md` and `RESULTS_FORMAT.md`). Aggregate client throughput is the **sum** of per-replica `achievedThroughputRps`. Cross-replica latency percentiles in this tool are **descriptive** (per-replica summaries); true merged percentiles require HDR histogram merge when logs are present.
