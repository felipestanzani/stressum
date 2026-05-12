# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | HIKARI_DISCIPLINED |
| **Workload** | W3_SLOW_QUERY |
| **Run time** | 2026-05-12T02:14:19Z |
| **Duration** | 1800 s |
| **Instances**| 8 |
| **Target RPS**| 200 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/hikari-prod-20260512-025608` |

---

## Aggregate Metrics (mean across 8 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 142.80 RPS (per instance) |
| **Total throughput** | 1142.37 RPS (all instances) |
| **p50 latency** | 0.46 ms |
| **p95 latency** | 5.88 ms |
| **p99 latency** | 87.63 ms |
| **p999 latency** | 2023.42 ms |
| **Error rate** | 0.00 |
| **Total requests** | 2878807 |
| **Failed requests** | 0 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 300 |
| observed_postgres_backends_max_numbackends | 266 |
| observed_postgres_backends_avg_numbackends | 199.30 |
| observed_postgres_backends_median_numbackends | 215 |
| observed_client_backends_active_median | 1832041 |
| observed_client_backends_active_max | 3904340 |
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
| **Bench JVM CPU (median)** | 0.77% | `OperatingSystemMXBean.getProcessCpuLoad()` |
| **Bench JVM GC pause total** | 892 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 50 ms | ✅ PASS (5.88 ms) |
| Error rate | < 0.1% | ✅ PASS (0.0000) |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 0.461 | 6.075 | 84.543 | 142.73089679375815 | 0 | 0.8132147920360749 | 167 |
| 1 | 0.452 | 5.795 | 88.447 | 142.85362817509713 | 0 | 0.7568590350047304 | 100 |
| 2 | 0.467 | 6.011 | 86.719 | 142.7415543429564 | 0 | 0.8209338122113904 | 125 |
| 3 | 0.463 | 5.675 | 89.087 | 142.8541950476006 | 0 | 0.7385524372230428 | 76 |
| 4 | 0.46 | 5.983 | 87.935 | 142.74002369820582 | 0 | 0.7996361902755889 | 137 |
| 5 | 0.451 | 5.619 | 88.383 | 142.85470525024246 | 0 | 0.7082154553254704 | 86 |
| 6 | 0.458 | 6.015 | 87.231 | 142.7414977000219 | 0 | 0.7959500251551234 | 124 |
| 7 | 0.441 | 5.867 | 88.703 | 142.85385492355869 | 0 | 0.7327796775769418 | 77 |
---
## PostgreSQL — Database Statistics

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 215 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 1832041 / 3904340 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 2013115874 | Cumulative since stats reset |
| Transactions rolled back | 0 | Non-zero → contention or application errors |
| Temp file bytes written | 1 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | 0 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 6100 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 269225 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> CPU% is normalised to a single core (100% = 1 CPU fully busy).
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | Avg CPU (%) | Peak CPU (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|-------------|--------------|---------------|----------------|
| PostgreSQL | db | 115.4 | 340.3 | 6711.4 | 18292.7 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-05-12T02:47:07Z*
