# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | HIKARI_DISCIPLINED |
| **Workload** | W3_SLOW_QUERY |
| **Run time** | 2026-05-11T22:39:41Z |
| **Duration** | 1800 s |
| **Instances**| 8 |
| **Target RPS**| 200 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/hikari-prod-20260511-232048` |

---

## Aggregate Metrics (mean across 8 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 142.74 RPS (per instance) |
| **Total throughput** | 1141.89 RPS (all instances) |
| **p50 latency** | 0.51 ms |
| **p95 latency** | 9.39 ms |
| **p99 latency** | 98.52 ms |
| **p999 latency** | 3726.86 ms |
| **Error rate** | 0.00 |
| **Total requests** | 2877627 |
| **Failed requests** | 0 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 300 |
| observed_postgres_backends_max_numbackends | 305 |
| observed_postgres_backends_avg_numbackends | 259.13 |
| observed_postgres_backends_median_numbackends | 305 |
| observed_client_backends_active_median | 1860649 |
| observed_client_backends_active_max | 3900204 |
| observed_client_backends_idle_median | 0 |
| observed_client_backends_idle_max | 0 |

## Topology-Specific Summary

| Field | Value |
|-------|-------|
| Scenario profile | hikari-prod |
| Configured replicas | 8 |
| Configured client pool size (per replica) | 38 |
| OJP servers | N/A |
| Real DB connections per OJP server | N/A |
| OJP proxy-tier CPU (avg / peak, summed) | N/A% / 0% |
| OJP proxy-tier RSS (avg / peak, summed) | N/A MiB / 0 MiB |
| PgBouncer nodes | N/A |
| PgBouncer server pool size per node | N/A |
| pgbouncer_reserve_pool_size | N/A |
| PgBouncer local HikariCP pool size per replica | N/A |
| HAProxy nodes | N/A |
| PgBouncer tier CPU (avg / peak, summed) | N/A% / 0% |
| PgBouncer tier RSS (avg / peak, summed) | N/A MiB / 0 MiB |
| HAProxy CPU (avg / peak, summed) | N/A% / 0% |
| HAProxy RSS (avg / peak, summed) | N/A MiB / 0 MiB |
| Total PgBouncer proxy-tier CPU (avg / peak) | N/A% / 0.00% |
| Total PgBouncer proxy-tier RSS (avg / peak) | N/A MiB / 0.00 MiB |

## Bench JVM System Metrics (in-process, median across instances)

| Metric | Value | Source |
|--------|-------|--------|
| **Bench JVM CPU (median)** | 0.75% | `OperatingSystemMXBean.getProcessCpuLoad()` |
| **Bench JVM GC pause total** | 817 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 50 ms | ✅ PASS (9.39 ms) |
| Error rate | < 0.1% | ✅ PASS (0.0000) |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 0.562 | 9.751 | 97.855 | 142.6185961868587 | 0 | 0.8241051280541154 | 119 |
| 1 | 0.465 | 9.159 | 99.263 | 142.85289122394883 | 0 | 0.6630961920719333 | 112 |
| 2 | 0.558 | 9.319 | 98.239 | 142.62097711845374 | 0 | 0.8251676121712224 | 126 |
| 3 | 0.474 | 9.495 | 98.751 | 142.85391163771297 | 0 | 0.6625891946992865 | 57 |
| 4 | 0.571 | 9.415 | 100.223 | 142.6232526542513 | 0 | 0.8311963293654826 | 133 |
| 5 | 0.452 | 9.279 | 95.743 | 142.85362817509713 | 0 | 0.6956522168528817 | 75 |
| 6 | 0.542 | 9.127 | 99.647 | 142.61452084789136 | 0 | 0.8232570650366727 | 118 |
| 7 | 0.465 | 9.559 | 98.431 | 142.8541383684935 | 0 | 0.6953067227864955 | 77 |
---
## PostgreSQL — Database Statistics

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 305 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 1860649 / 3900204 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 2010724381 | Cumulative since stats reset |
| Transactions rolled back | 0 | Non-zero → contention or application errors |
| Temp file bytes written | 1 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | 0 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 7036 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 269893 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> CPU% is normalised to a single core (100% = 1 CPU fully busy).
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | Avg CPU (%) | Peak CPU (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|-------------|--------------|---------------|----------------|
| PostgreSQL | db | 96.2 | 336.6 | 7645.0 | 22925.8 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-05-11T23:12:31Z*
