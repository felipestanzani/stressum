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

## Compare multiple runs (cross-scenario)

Create a JSON config (by default **`stressum-comparison.json`** at the repository root, or pass `--config`). Each `path` is resolved **relative to the directory containing the config file**. At least two runs are required.

```json
{
  "runs": [
    { "path": "results/hikari-prod-20260511-232048", "label": "Hikari" },
    { "path": "results/ojp-prod-20260512-044306" }
  ]
}
```

```bash
uv run stressum compare
# or
uv run stressum compare --config /path/to/my-comparison.json --out /path/to/output-dir
```

Output defaults to `<project-root>/output/comparison-<YYYY-MM-dd-HHMMSS-microseconds>/` and includes:

- `comparison_metadata.json` — scenarios, paths, HDR merge status, fairness warnings when `workload` / `loadMode` / `targetRps` differ across runs
- `comparison_summary.csv` — one row per run (throughput, error rate, median replica percentiles, optional **merged** percentiles when `.hlog` HDR logs exist)
- PNG figures: total throughput, latency (HDR merged across replicas **within** each run when logs are present; otherwise median of `summary.json` percentiles), error rate, optional open-loop / PostgreSQL backends / JVM heap / timeseries plots when data exists

`--no-plots` and `--seed` behave like the single-run command.

## Interpretation

See `stressar-docs/` (especially `METRICS.md` and `RESULTS_FORMAT.md`). Aggregate client throughput is the **sum** of per-replica `achievedThroughputRps`. In **`compare`**, latency bars use **HDR histogram merge across replicas** when readable `.hlog` files are found under each run; otherwise they use the **median** of per-replica `summary.json` percentiles (indicative only). Single-run `stressum <run>` figures remain per-replica / median summaries unless you use `compare`.
