# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | OJP |
| **Workload** | W3_SLOW_QUERY |
| **Run time** | 2026-05-12T01:21:26Z |
| **Duration** | 1800 s |
| **Instances**| 8 |
| **Target RPS**| 200 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/ojp-sqs-prod-20260512-020256` |

---

## Aggregate Metrics (mean across 8 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 139.63 RPS (per instance) |
| **Total throughput** | 1117.03 RPS (all instances) |
| **p50 latency** | 8.54 ms |
| **p95 latency** | 34.70 ms |
| **p99 latency** | 193.25 ms |
| **p999 latency** | 56297.50 ms |
| **Error rate** | 0.00 |
| **Total requests** | 2834054 |
| **Failed requests** | 7902 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 48 |
| observed_postgres_backends_max_numbackends | 49 |
| observed_postgres_backends_avg_numbackends | 48.63 |
| observed_postgres_backends_median_numbackends | 49 |
| observed_client_backends_active_median | 1685707 |
| observed_client_backends_active_max | 3741202 |
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
| OJP proxy-tier CPU (avg / peak, summed) | 145.30% / 807.90% |
| OJP proxy-tier RSS (avg / peak, summed) | 1059.40 MiB / 1163.10 MiB |
| PgBouncer nodes | N/A |
| PgBouncer server pool size per node | N/A |
| pgbouncer_reserve_pool_size | N/A |
| PgBouncer local HikariCP pool size per replica | N/A |
| HAProxy nodes | N/A |
| PgBouncer tier CPU (avg / peak, summed) | 145.30% / 807.90% |
| PgBouncer tier RSS (avg / peak, summed) | 1059.40 MiB / 1163.10 MiB |
| HAProxy CPU (avg / peak, summed) | N/A% / 0% |
| HAProxy RSS (avg / peak, summed) | N/A MiB / 0 MiB |
| Total PgBouncer proxy-tier CPU (avg / peak) | 145.30% / 807.90% |
| Total PgBouncer proxy-tier RSS (avg / peak) | 1059.40 MiB / 1163.10 MiB |

## Bench JVM System Metrics (in-process, median across instances)

| Metric | Value | Source |
|--------|-------|--------|
| **Bench JVM CPU (median)** | 12.29% | `OperatingSystemMXBean.getProcessCpuLoad()` |
| **Bench JVM GC pause total** | 36443 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 50 ms | ✅ PASS (34.70 ms) |
| Error rate | < 0.1% | ✅ PASS (0.0000) |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 6.267 | 20.991 | 182.527 | 148.11585495996144 | 0.0024861849040130326 | 7.28783010311111 | 4429 |
| 1 | 13.143 | 44.415 | 209.407 | 156.88438290369385 | 0.00266089093362346 | 21.2086980883723 | 5347 |
| 2 | 5.335 | 25.231 | 173.951 | 131.34553353725414 | 0.00334405028971772 | 4.891613447820161 | 4247 |
| 3 | 10.151 | 48.543 | 209.919 | 136.75595408662767 | 0.0025915174646368847 | 16.287342073398765 | 4468 |
| 4 | 5.539 | 18.479 | 170.879 | 153.21864730885466 | 0.00233685147867623 | 10.803364205640218 | 4409 |
| 5 | 10.599 | 57.119 | 208.511 | 127.23798155782251 | 0.0033035283044571314 | 14.610715344170881 | 4789 |
| 6 | 5.163 | 17.599 | 172.927 | 138.08959551508607 | 0.0028227544260732316 | 9.766749075862052 | 3758 |
| 7 | 12.151 | 45.215 | 217.855 | 125.37789963491605 | 0.002926292629262926 | 13.461666583387466 | 4996 |

---

## Error Breakdown

| Instance | Error type | Count | First error message |
|----------|------------|-------|---------------------|
| 0 | other | 30 | — |
| 0 | sql_exception | 904 | Connection acquisition failed for hash: ZVX5K7dkIEn0vc4JUjIuRAhqUKjPpHaHD144ERumYnI. Pool state - Active: 16, Max: 16, Waiting threads: 15. Original error: OJP-Pool-default-hikari - Connection is not available, request timed out after 30000ms (total=16, active=16, idle=0, waiting=15) |
| 1 | other | 35 | — |
| 1 | sql_exception | 1024 | Connection acquisition failed for hash: ZVX5K7dkIEn0vc4JUjIuRAhqUKjPpHaHD144ERumYnI. Pool state - Active: 16, Max: 16, Waiting threads: 15. Original error: OJP-Pool-default-hikari - Connection is not available, request timed out after 30000ms (total=16, active=16, idle=0, waiting=15) |
| 2 | other | 36 | — |
| 2 | sql_exception | 1079 | Connection acquisition failed for hash: ZVX5K7dkIEn0vc4JUjIuRAhqUKjPpHaHD144ERumYnI. Pool state - Active: 16, Max: 16, Waiting threads: 15. Original error: OJP-Pool-default-hikari - Connection is not available, request timed out after 30000ms (total=16, active=16, idle=0, waiting=15) |
| 3 | other | 39 | — |
| 3 | sql_exception | 859 | Connection acquisition failed for hash: ZVX5K7dkIEn0vc4JUjIuRAhqUKjPpHaHD144ERumYnI. Pool state - Active: 16, Max: 16, Waiting threads: 14. Original error: OJP-Pool-default-hikari - Connection is not available, request timed out after 30000ms (total=16, active=16, idle=0, waiting=14) |
| 4 | other | 40 | — |
| 4 | sql_exception | 868 | Connection acquisition failed for hash: ZVX5K7dkIEn0vc4JUjIuRAhqUKjPpHaHD144ERumYnI. Pool state - Active: 16, Max: 16, Waiting threads: 15. Original error: OJP-Pool-default-hikari - Connection is not available, request timed out after 30000ms (total=16, active=16, idle=0, waiting=15) |
| 5 | other | 35 | — |
| 5 | sql_exception | 1032 | Connection acquisition failed for hash: ZVX5K7dkIEn0vc4JUjIuRAhqUKjPpHaHD144ERumYnI. Pool state - Active: 16, Max: 16, Waiting threads: 15. Original error: OJP-Pool-default-hikari - Connection is not available, request timed out after 30000ms (total=16, active=16, idle=0, waiting=15) |
| 6 | other | 40 | — |
| 6 | sql_exception | 949 | Connection acquisition failed for hash: ZVX5K7dkIEn0vc4JUjIuRAhqUKjPpHaHD144ERumYnI. Pool state - Active: 16, Max: 16, Waiting threads: 15. Original error: OJP-Pool-default-hikari - Connection is not available, request timed out after 30000ms (total=16, active=16, idle=0, waiting=15) |
| 7 | other | 40 | — |
| 7 | sql_exception | 891 | Unexpected error: Timeout waiting for fast operation slot for operation: e7282124a6fbdd3c |
---
## OJP Proxy — JVM Heap and GC Metrics

> **Note:** Heap values are from `jstat -gc` (actual in-use JVM heap).
> OS RSS is **not** used here because the JVM does not return memory to the OS after GC.

| Proxy host | Heap used — median (MB) | Heap committed — median (MB) | Total GC time (s) | Young GC count | Full GC count |
|------------|------------------------|------------------------------|-------------------|----------------|---------------|
| ojp-1 | 32.4 | 81.0 | 2.319 | 866 | 0 |
| ojp-2 | 34.7 | 64.0 | 11.166 | 5936 | 0 |
| ojp-3 | 34.4 | 64.0 | 8.492 | 3942 | 0 |
---
## PostgreSQL — Database Statistics

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 49 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 1685707 / 3741202 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 1925774323 | Cumulative since stats reset |
| Transactions rolled back | 0 | Non-zero → contention or application errors |
| Temp file bytes written | 1 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | 48 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 4337 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 269214 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> CPU% is normalised to a single core (100% = 1 CPU fully busy).
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | Avg CPU (%) | Peak CPU (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|-------------|--------------|---------------|----------------|
| Proxy (OJP / pgBouncer) | ojp-1 | 28.9 | 270.7 | 341.2 | 377.0 |
| Proxy (OJP / pgBouncer) | ojp-2 | 69.4 | 240.6 | 389.9 | 449.6 |
| Proxy (OJP / pgBouncer) | ojp-3 | 47.0 | 296.6 | 328.3 | 336.5 |
| PostgreSQL | db | 174.8 | 349.9 | 3803.8 | 3985.3 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-05-12T01:54:50Z*
