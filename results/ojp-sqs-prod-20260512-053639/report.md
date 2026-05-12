# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | OJP |
| **Workload** | W3_SLOW_QUERY |
| **Run time** | 2026-05-12T04:55:08Z |
| **Duration** | 1800 s |
| **Instances**| 8 |
| **Target RPS**| 200 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/ojp-sqs-prod-20260512-053639` |

---

## Aggregate Metrics (mean across 8 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 130.28 RPS (per instance) |
| **Total throughput** | 1042.23 RPS (all instances) |
| **p50 latency** | 9.84 ms |
| **p95 latency** | 36.16 ms |
| **p99 latency** | 190.91 ms |
| **p999 latency** | 52650.12 ms |
| **Error rate** | 0.00 |
| **Total requests** | 2645390 |
| **Failed requests** | 8464 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 48 |
| observed_postgres_backends_max_numbackends | 49 |
| observed_postgres_backends_avg_numbackends | 48.64 |
| observed_postgres_backends_median_numbackends | 49 |
| observed_client_backends_active_median | 1662900 |
| observed_client_backends_active_max | 3566711 |
| observed_client_backends_idle_median | 0 |
| observed_client_backends_idle_max | 0 |

## Topology-Specific Summary

| Field | Value |
|-------|-------|
| Scenario profile | ojp-sqs-prod |
| Configured replicas | 8 |
| Configured client pool size (per replica) | 48 |
| OJP servers | 3 |
| Real DB connections per OJP server | 16 |
| OJP proxy-tier CPU (avg / peak, summed) | 137.30% / 768.30% |
| OJP proxy-tier RSS (avg / peak, summed) | 1065.00 MiB / 1117.40 MiB |
| PgBouncer nodes | N/A |
| PgBouncer server pool size per node | N/A |
| pgbouncer_reserve_pool_size | N/A |
| PgBouncer local HikariCP pool size per replica | N/A |
| HAProxy nodes | N/A |
| PgBouncer tier CPU (avg / peak, summed) | 137.30% / 768.30% |
| PgBouncer tier RSS (avg / peak, summed) | 1065.00 MiB / 1117.40 MiB |
| HAProxy CPU (avg / peak, summed) | N/A% / 0% |
| HAProxy RSS (avg / peak, summed) | N/A MiB / 0 MiB |
| Total PgBouncer proxy-tier CPU (avg / peak) | 137.30% / 768.30% |
| Total PgBouncer proxy-tier RSS (avg / peak) | 1065.00 MiB / 1117.40 MiB |

## Bench JVM System Metrics (in-process, median across instances)

| Metric | Value | Source |
|--------|-------|--------|
| **Bench JVM CPU (median)** | 9.45% | `OperatingSystemMXBean.getProcessCpuLoad()` |
| **Bench JVM GC pause total** | 35392 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 50 ms | ✅ PASS (36.16 ms) |
| Error rate | < 0.1% | ✅ PASS (0.0000) |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 4.807 | 13.991 | 160.895 | 126.93186049103701 | 0.003466102326043244 | 3.0088502118283786 | 3739 |
| 1 | 16.991 | 64.831 | 208.127 | 162.54432603090135 | 0.0023627586541493826 | 21.250277989579367 | 5195 |
| 2 | 4.751 | 22.703 | 159.615 | 139.96251466370705 | 0.003203368885661124 | 9.077810240140952 | 4006 |
| 3 | 12.167 | 46.303 | 230.527 | 118.1958636368487 | 0.0034523781753714807 | 9.27310610688059 | 4955 |
| 4 | 5.075 | 19.151 | 171.007 | 114.89044661260965 | 0.00414883740051869 | 0.9994699926349626 | 3595 |
| 5 | 12.999 | 52.415 | 202.623 | 132.1211177436127 | 0.003163905828326052 | 15.779926005489916 | 5031 |
| 6 | 5.391 | 15.199 | 182.143 | 111.23091498584421 | 0.003311422459590021 | 0.3886876541047187 | 3725 |
| 7 | 16.527 | 54.655 | 212.351 | 136.35071912376344 | 0.002867284057669407 | 15.810754541934823 | 5146 |

---

## Error Breakdown

| Instance | Error type | Count | First error message |
|----------|------------|-------|---------------------|
| 0 | other | 40 | — |
| 0 | sql_exception | 1077 | Connection acquisition failed for hash: ZVX5K7dkIEn0vc4JUjIuRAhqUKjPpHaHD144ERumYnI. Pool state - Active: 16, Max: 16, Waiting threads: 13. Original error: OJP-Pool-default-hikari - Connection is not available, request timed out after 30000ms (total=16, active=16, idle=0, waiting=13) |
| 1 | other | 40 | — |
| 1 | sql_exception | 934 | Connection acquisition failed for hash: ZVX5K7dkIEn0vc4JUjIuRAhqUKjPpHaHD144ERumYnI. Pool state - Active: 16, Max: 16, Waiting threads: 13. Original error: OJP-Pool-default-hikari - Connection is not available, request timed out after 30000ms (total=16, active=16, idle=0, waiting=13) |
| 2 | other | 40 | — |
| 2 | sql_exception | 1098 | Connection acquisition failed for hash: ZVX5K7dkIEn0vc4JUjIuRAhqUKjPpHaHD144ERumYnI. Pool state - Active: 16, Max: 16, Waiting threads: 13. Original error: OJP-Pool-default-hikari - Connection is not available, request timed out after 30000ms (total=16, active=16, idle=0, waiting=13) |
| 3 | other | 38 | — |
| 3 | sql_exception | 998 | Connection acquisition failed for hash: ZVX5K7dkIEn0vc4JUjIuRAhqUKjPpHaHD144ERumYnI. Pool state - Active: 16, Max: 16, Waiting threads: 13. Original error: OJP-Pool-default-hikari - Connection is not available, request timed out after 30000ms (total=16, active=16, idle=0, waiting=13) |
| 4 | other | 40 | — |
| 4 | sql_exception | 1171 | Connection acquisition failed for hash: ZVX5K7dkIEn0vc4JUjIuRAhqUKjPpHaHD144ERumYnI. Pool state - Active: 16, Max: 16, Waiting threads: 13. Original error: OJP-Pool-default-hikari - Connection is not available, request timed out after 30000ms (total=16, active=16, idle=0, waiting=13) |
| 5 | other | 33 | — |
| 5 | sql_exception | 1028 | Connection acquisition failed for hash: ZVX5K7dkIEn0vc4JUjIuRAhqUKjPpHaHD144ERumYnI. Pool state - Active: 16, Max: 16, Waiting threads: 13. Original error: OJP-Pool-default-hikari - Connection is not available, request timed out after 30000ms (total=16, active=16, idle=0, waiting=13) |
| 6 | other | 40 | — |
| 6 | sql_exception | 895 | Connection acquisition failed for hash: ZVX5K7dkIEn0vc4JUjIuRAhqUKjPpHaHD144ERumYnI. Pool state - Active: 16, Max: 16, Waiting threads: 13. Original error: OJP-Pool-default-hikari - Connection is not available, request timed out after 30000ms (total=16, active=16, idle=0, waiting=13) |
| 7 | other | 40 | — |
| 7 | sql_exception | 952 | Unexpected error: Timeout waiting for fast operation slot for operation: e7282124a6fbdd3c |
---
## OJP Proxy — JVM Heap and GC Metrics

> **Note:** Heap values are from `jstat -gc` (actual in-use JVM heap).
> OS RSS is **not** used here because the JVM does not return memory to the OS after GC.

| Proxy host | Heap used — median (MB) | Heap committed — median (MB) | Total GC time (s) | Young GC count | Full GC count |
|------------|------------------------|------------------------------|-------------------|----------------|---------------|
| ojp-1 | 33.5 | 53.0 | 2.411 | 1159 | 0 |
| ojp-2 | 38.1 | 76.0 | 9.887 | 5582 | 0 |
| ojp-3 | 34.7 | 64.0 | 7.755 | 3928 | 0 |
---
## PostgreSQL — Database Statistics

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 49 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 1662900 / 3566711 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 1840003948 | Cumulative since stats reset |
| Transactions rolled back | 0 | Non-zero → contention or application errors |
| Temp file bytes written | 1 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | 48 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 6109 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 269087 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> CPU% is normalised to a single core (100% = 1 CPU fully busy).
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | Avg CPU (%) | Peak CPU (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|-------------|--------------|---------------|----------------|
| Proxy (OJP / pgBouncer) | ojp-1 | 27.1 | 228.1 | 359.7 | 382.0 |
| Proxy (OJP / pgBouncer) | ojp-2 | 67.2 | 267.3 | 381.1 | 401.8 |
| Proxy (OJP / pgBouncer) | ojp-3 | 43.0 | 272.9 | 324.2 | 333.6 |
| PostgreSQL | db | 171.1 | 350.4 | 3802.6 | 3996.1 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-05-12T05:28:26Z*
