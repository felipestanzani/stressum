# Stressar results — documentation for analysis

This repository consumes **exported Stressar benchmark bundles** (for example under `../results/`). The files here explain **what was measured**, **how artifacts are structured**, and **how the official benchmark protocol maps to fields** in `summary.json`, CSV exports, and reports.

Operational guides (installation, deployment, Ansible, full YAML config) live with the upstream Stressar / benchmark harness project and are intentionally **not** vendored here, to keep context focused on analysis.

## Documents in this folder

| Document | Use it when you need to… |
|----------|---------------------------|
| [RESULTS_FORMAT.md](RESULTS_FORMAT.md) | Parse schemas: `summary.json`, timeseries CSV, HDR logs, aggregated outputs, metadata. |
| [METRICS.md](METRICS.md) | Understand definitions, collection scope, latency clock, histogram design, and caveats. |
| [BENCHMARKING_GUIDE.md](BENCHMARKING_GUIDE.md) | Interpret scenario names, SUTs (Hikari / OJP / PgBouncer), workloads (W1–W3), topology, and test protocols (capacity sweep vs overload/recovery). |

## Stressar in one sentence

Stressar is a JDBC-oriented PostgreSQL stress tool used to compare connection strategies (direct HikariCP pools vs OJP vs PgBouncer) under controlled load, with multi-replica clients and rich latency/throughput metrics.
