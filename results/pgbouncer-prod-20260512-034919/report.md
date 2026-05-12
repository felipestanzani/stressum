# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | PGBOUNCER |
| **Workload** | W3_SLOW_QUERY |
| **Run time** | 2026-05-12T03:08:08Z |
| **Duration** | 1800 s |
| **Instances**| 8 |
| **Target RPS**| 200 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/pgbouncer-prod-20260512-034919` |

---

## Aggregate Metrics (mean across 8 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 142.82 RPS (per instance) |
| **Total throughput** | 1142.60 RPS (all instances) |
| **p50 latency** | 1.03 ms |
| **p95 latency** | 21.74 ms |
| **p99 latency** | 166.46 ms |
| **p999 latency** | 1897.46 ms |
| **Error rate** | 0.00 |
| **Total requests** | 2879391 |
| **Failed requests** | 0 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 48 |
| observed_postgres_backends_max_numbackends | 49 |
| observed_postgres_backends_avg_numbackends | 48.51 |
| observed_postgres_backends_median_numbackends | 49 |
| observed_client_backends_active_median | 1822557 |
| observed_client_backends_active_max | 3904622 |
| observed_client_backends_idle_median | 0 |
| observed_client_backends_idle_max | 0 |

## Topology-Specific Summary

| Field | Value |
|-------|-------|
| Scenario profile | pgbouncer-prod |
| Configured replicas | 8 |
| Configured client pool size (per replica) | 20 |
| OJP servers | N/A |
| Real DB connections per OJP server | N/A |
| OJP proxy-tier CPU (avg / peak, summed) | 10.80% / 24.90% |
| OJP proxy-tier RSS (avg / peak, summed) | 34.20 MiB / 34.20 MiB |
| PgBouncer nodes | 3 |
| PgBouncer server pool size per node | 16 |
| pgbouncer_reserve_pool_size | 0 |
| PgBouncer local HikariCP pool size per replica | 20 |
| HAProxy nodes | 1 |
| PgBouncer tier CPU (avg / peak, summed) | 10.80% / 24.90% |
| PgBouncer tier RSS (avg / peak, summed) | 34.20 MiB / 34.20 MiB |
| HAProxy CPU (avg / peak, summed) | 11.40% / 19.80% |
| HAProxy RSS (avg / peak, summed) | 22.40 MiB / 22.50 MiB |
| Total PgBouncer proxy-tier CPU (avg / peak) | 22.20% / 44.70% |
| Total PgBouncer proxy-tier RSS (avg / peak) | 56.60 MiB / 56.70 MiB |

## Bench JVM System Metrics (in-process, median across instances)

| Metric | Value | Source |
|--------|-------|--------|
| **Bench JVM CPU (median)** | 0.70% | `OperatingSystemMXBean.getProcessCpuLoad()` |
| **Bench JVM GC pause total** | 639 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 50 ms | ✅ PASS (21.74 ms) |
| Error rate | < 0.1% | ✅ PASS (0.0000) |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 1.059 | 21.983 | 169.855 | 142.79858351005066 | 0 | 0.7696254489481785 | 94 |
| 1 | 1.008 | 22.175 | 168.959 | 142.8554421971167 | 0 | 0.6602336211274759 | 60 |
| 2 | 1.044 | 22.751 | 166.399 | 142.7923477101463 | 0 | 0.7420236586189514 | 99 |
| 3 | 1.018 | 22.079 | 166.399 | 142.85527213334112 | 0 | 0.6177606586902838 | 66 |
| 4 | 1.049 | 21.455 | 158.591 | 142.79195088947353 | 0 | 0.769822991414541 | 92 |
| 5 | 1.014 | 21.391 | 165.247 | 142.85521544015202 | 0 | 0.6480558325024925 | 66 |
| 6 | 1.041 | 20.783 | 162.431 | 142.79433303479772 | 0 | 0.7585347142309167 | 94 |
| 7 | 0.983 | 21.295 | 173.823 | 142.85561226554879 | 0 | 0.645481787734564 | 68 |
---
## PostgreSQL — Database Statistics

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 49 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 1822557 / 3904622 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 2013547565 | Cumulative since stats reset |
| Transactions rolled back | 0 | Non-zero → contention or application errors |
| Temp file bytes written | 1 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | 48 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 1930 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 269197 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> CPU% is normalised to a single core (100% = 1 CPU fully busy).
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | Avg CPU (%) | Peak CPU (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|-------------|--------------|---------------|----------------|
| Proxy (OJP / pgBouncer) | pgbouncer-1 | 3.8 | 8.6 | 11.4 | 11.4 |
| Proxy (OJP / pgBouncer) | pgbouncer-2 | 3.3 | 7.7 | 11.4 | 11.4 |
| Proxy (OJP / pgBouncer) | pgbouncer-3 | 3.7 | 8.6 | 11.4 | 11.4 |
| PostgreSQL | db | 202.6 | 359.5 | 3521.2 | 3895.6 |
| HAProxy | lb | 11.4 | 19.8 | 22.4 | 22.5 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-05-12T03:41:11Z*
