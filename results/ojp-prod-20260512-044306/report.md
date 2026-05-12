# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | OJP |
| **Workload** | W3_SLOW_QUERY |
| **Run time** | 2026-05-12T04:01:32Z |
| **Duration** | 1800 s |
| **Instances**| 8 |
| **Target RPS**| 200 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/ojp-prod-20260512-044306` |

---

## Aggregate Metrics (mean across 8 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 126.23 RPS (per instance) |
| **Total throughput** | 1009.87 RPS (all instances) |
| **p50 latency** | 10.85 ms |
| **p95 latency** | 42.26 ms |
| **p99 latency** | 225.33 ms |
| **p999 latency** | 30066.75 ms |
| **Error rate** | 0.00 |
| **Total requests** | 2567133 |
| **Failed requests** | 12073 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 48 |
| observed_postgres_backends_max_numbackends | 49 |
| observed_postgres_backends_avg_numbackends | 48.65 |
| observed_postgres_backends_median_numbackends | 49 |
| observed_client_backends_active_median | 1533595 |
| observed_client_backends_active_max | 3335405 |
| observed_client_backends_idle_median | 0 |
| observed_client_backends_idle_max | 0 |

## Topology-Specific Summary

| Field | Value |
|-------|-------|
| Scenario profile | ojp-prod |
| Configured replicas | 8 |
| Configured client pool size (per replica) | 48 |
| OJP servers | 3 |
| Real DB connections per OJP server | 16 |
| OJP proxy-tier CPU (avg / peak, summed) | 130.90% / 785.80% |
| OJP proxy-tier RSS (avg / peak, summed) | 1042.10 MiB / 1097.50 MiB |
| PgBouncer nodes | N/A |
| PgBouncer server pool size per node | N/A |
| pgbouncer_reserve_pool_size | N/A |
| PgBouncer local HikariCP pool size per replica | N/A |
| HAProxy nodes | N/A |
| PgBouncer tier CPU (avg / peak, summed) | 130.90% / 785.80% |
| PgBouncer tier RSS (avg / peak, summed) | 1042.10 MiB / 1097.50 MiB |
| HAProxy CPU (avg / peak, summed) | N/A% / 0% |
| HAProxy RSS (avg / peak, summed) | N/A MiB / 0 MiB |
| Total PgBouncer proxy-tier CPU (avg / peak) | 130.90% / 785.80% |
| Total PgBouncer proxy-tier RSS (avg / peak) | 1042.10 MiB / 1097.50 MiB |

## Bench JVM System Metrics (in-process, median across instances)

| Metric | Value | Source |
|--------|-------|--------|
| **Bench JVM CPU (median)** | 9.38% | `OperatingSystemMXBean.getProcessCpuLoad()` |
| **Bench JVM GC pause total** | 35303 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 50 ms | ✅ PASS (42.26 ms) |
| Error rate | < 0.1% | ✅ PASS (0.0000) |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 5.371 | 19.535 | 209.535 | 124.27779248959523 | 0.005144592798835664 | 1.2626625341756619 | 3736 |
| 1 | 21.231 | 74.367 | 251.263 | 148.39478242035176 | 0.003275972836504001 | 21.43689776797489 | 5518 |
| 2 | 4.975 | 31.167 | 212.479 | 102.11319376594797 | 0.006441514890475018 | 0.52523094713705 | 3337 |
| 3 | 9.999 | 44.927 | 229.119 | 134.23925201434568 | 0.004677128664996264 | 15.585109382931122 | 5220 |
| 4 | 4.455 | 18.831 | 199.935 | 124.24948470314357 | 0.005249634519115758 | 3.168120167429648 | 3283 |
| 5 | 20.655 | 71.871 | 255.743 | 135.73410705738624 | 0.0037104728749637367 | 15.9103923246259 | 5188 |
| 6 | 3.967 | 19.039 | 204.031 | 99.40504163285698 | 0.0067610261594843925 | 0.7521417858461791 | 3535 |
| 7 | 16.151 | 58.303 | 240.511 | 141.45515887194438 | 0.0035970221556519463 | 16.42368326398804 | 5486 |

---

## Error Breakdown

| Instance | Error type | Count | First error message |
|----------|------------|-------|---------------------|
| 0 | other | 40 | — |
| 0 | sql_exception | 1586 | Unexpected error: Timeout waiting for admission control slot for operation: e7282124a6fbdd3c |
| 1 | other | 36 | — |
| 1 | sql_exception | 1198 | Unexpected error: Timeout waiting for admission control slot for operation: e7282124a6fbdd3c |
| 2 | other | 40 | — |
| 2 | sql_exception | 1635 | Unexpected error: Timeout waiting for admission control slot for operation: e7282124a6fbdd3c |
| 3 | other | 38 | — |
| 3 | sql_exception | 1558 | Unexpected error: Timeout waiting for admission control slot for operation: e7282124a6fbdd3c |
| 4 | other | 40 | — |
| 4 | sql_exception | 1619 | Unexpected error: Timeout waiting for admission control slot for operation: e7282124a6fbdd3c |
| 5 | other | 40 | — |
| 5 | sql_exception | 1239 | Unexpected error: Timeout waiting for admission control slot for operation: e7282124a6fbdd3c |
| 6 | other | 40 | — |
| 6 | sql_exception | 1672 | Unexpected error: Timeout waiting for admission control slot for operation: e7282124a6fbdd3c |
| 7 | other | 35 | — |
| 7 | sql_exception | 1257 | Unexpected error: Timeout waiting for admission control slot for operation: e7282124a6fbdd3c |
---
## OJP Proxy — JVM Heap and GC Metrics

> **Note:** Heap values are from `jstat -gc` (actual in-use JVM heap).
> OS RSS is **not** used here because the JVM does not return memory to the OS after GC.

| Proxy host | Heap used — median (MB) | Heap committed — median (MB) | Total GC time (s) | Young GC count | Full GC count |
|------------|------------------------|------------------------------|-------------------|----------------|---------------|
| ojp-1 | 32.5 | 64.0 | 2.552 | 1192 | 0 |
| ojp-2 | 37.2 | 64.0 | 10.423 | 5922 | 0 |
| ojp-3 | 33.1 | 64.0 | 7.832 | 3804 | 0 |
---
## PostgreSQL — Database Statistics

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 49 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 1533595 / 3335405 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 1720151473 | Cumulative since stats reset |
| Transactions rolled back | 0 | Non-zero → contention or application errors |
| Temp file bytes written | 1 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | 48 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 4198 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 269037 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> CPU% is normalised to a single core (100% = 1 CPU fully busy).
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | Avg CPU (%) | Peak CPU (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|-------------|--------------|---------------|----------------|
| Proxy (OJP / pgBouncer) | ojp-1 | 29.4 | 274.6 | 378.0 | 397.9 |
| Proxy (OJP / pgBouncer) | ojp-2 | 60.6 | 212.3 | 345.1 | 371.5 |
| Proxy (OJP / pgBouncer) | ojp-3 | 40.9 | 298.9 | 319.0 | 328.1 |
| PostgreSQL | db | 156.3 | 333.6 | 3831.8 | 4020.9 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-05-12T04:34:54Z*
