# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | PGBOUNCER |
| **Workload** | W3_SLOW_QUERY |
| **Run time** | 2026-05-11T23:33:54Z |
| **Duration** | 1800 s |
| **Instances**| 8 |
| **Target RPS**| 200 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/pgbouncer-prod-20260512-001532` |

---

## Aggregate Metrics (mean across 8 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 142.81 RPS (per instance) |
| **Total throughput** | 1142.46 RPS (all instances) |
| **p50 latency** | 0.98 ms |
| **p95 latency** | 44.60 ms |
| **p99 latency** | 203.28 ms |
| **p999 latency** | 2295.81 ms |
| **Error rate** | 0.00 |
| **Total requests** | 2879032 |
| **Failed requests** | 0 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 48 |
| observed_postgres_backends_max_numbackends | 49 |
| observed_postgres_backends_avg_numbackends | 48.46 |
| observed_postgres_backends_median_numbackends | 49 |
| observed_client_backends_active_median | 1818157 |
| observed_client_backends_active_max | 3904338 |
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
| OJP proxy-tier CPU (avg / peak, summed) | 10.90% / 26.00% |
| OJP proxy-tier RSS (avg / peak, summed) | 34.10 MiB / 34.10 MiB |
| PgBouncer nodes | 3 |
| PgBouncer server pool size per node | 16 |
| pgbouncer_reserve_pool_size | 0 |
| PgBouncer local HikariCP pool size per replica | 20 |
| HAProxy nodes | 1 |
| PgBouncer tier CPU (avg / peak, summed) | 10.90% / 26.00% |
| PgBouncer tier RSS (avg / peak, summed) | 34.10 MiB / 34.10 MiB |
| HAProxy CPU (avg / peak, summed) | 10.70% / 20.80% |
| HAProxy RSS (avg / peak, summed) | 22.40 MiB / 22.50 MiB |
| Total PgBouncer proxy-tier CPU (avg / peak) | 21.60% / 46.80% |
| Total PgBouncer proxy-tier RSS (avg / peak) | 56.50 MiB / 56.60 MiB |

## Bench JVM System Metrics (in-process, median across instances)

| Metric | Value | Source |
|--------|-------|--------|
| **Bench JVM CPU (median)** | 0.68% | `OperatingSystemMXBean.getProcessCpuLoad()` |
| **Bench JVM GC pause total** | 706 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 50 ms | ✅ PASS (44.60 ms) |
| Error rate | < 0.1% | ✅ PASS (0.0000) |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 1.001 | 46.815 | 207.743 | 142.76428648808877 | 0 | 0.761808220874087 | 92 |
| 1 | 0.97 | 47.007 | 204.415 | 142.85442179786168 | 0 | 0.6131834440470108 | 67 |
| 2 | 0.987 | 45.279 | 205.183 | 142.7630393702912 | 0 | 0.7475704426332364 | 109 |
| 3 | 0.96 | 45.407 | 210.175 | 142.8543651179448 | 0 | 0.6134969325153374 | 70 |
| 4 | 0.997 | 43.423 | 200.063 | 142.75793733464917 | 0 | 0.7207207684719978 | 99 |
| 5 | 0.98 | 44.095 | 195.967 | 142.85493199472228 | 0 | 0.6136538371016584 | 66 |
| 6 | 0.99 | 42.687 | 202.111 | 142.75697402135134 | 0 | 0.7203499319070887 | 127 |
| 7 | 0.965 | 42.111 | 200.575 | 142.85521544015202 | 0 | 0.6141248720573182 | 76 |
---
## PostgreSQL — Database Statistics

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 49 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 1818157 / 3904338 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 2013420048 | Cumulative since stats reset |
| Transactions rolled back | 0 | Non-zero → contention or application errors |
| Temp file bytes written | 1 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | 48 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 6105 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 269286 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> CPU% is normalised to a single core (100% = 1 CPU fully busy).
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | Avg CPU (%) | Peak CPU (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|-------------|--------------|---------------|----------------|
| Proxy (OJP / pgBouncer) | pgbouncer-1 | 3.5 | 8.7 | 11.4 | 11.4 |
| Proxy (OJP / pgBouncer) | pgbouncer-2 | 3.4 | 7.7 | 11.4 | 11.4 |
| Proxy (OJP / pgBouncer) | pgbouncer-3 | 4.0 | 9.6 | 11.3 | 11.3 |
| PostgreSQL | db | 208.6 | 361.5 | 3506.2 | 3869.9 |
| HAProxy | lb | 10.7 | 20.8 | 22.4 | 22.5 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-05-12T00:06:52Z*
