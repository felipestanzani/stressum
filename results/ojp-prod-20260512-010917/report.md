# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | OJP |
| **Workload** | W3_SLOW_QUERY |
| **Run time** | 2026-05-12T00:27:46Z |
| **Duration** | 1800 s |
| **Instances**| 8 |
| **Target RPS**| 200 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/ojp-prod-20260512-010917` |

---

## Aggregate Metrics (mean across 8 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 129.02 RPS (per instance) |
| **Total throughput** | 1032.13 RPS (all instances) |
| **p50 latency** | 10.38 ms |
| **p95 latency** | 44.17 ms |
| **p99 latency** | 220.78 ms |
| **p999 latency** | 30060.62 ms |
| **Error rate** | 0.00 |
| **Total requests** | 2623413 |
| **Failed requests** | 12016 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 48 |
| observed_postgres_backends_max_numbackends | 49 |
| observed_postgres_backends_avg_numbackends | 48.65 |
| observed_postgres_backends_median_numbackends | 49 |
| observed_client_backends_active_median | 1560232 |
| observed_client_backends_active_max | 3377489 |
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
| OJP proxy-tier CPU (avg / peak, summed) | 139.60% / 833.20% |
| OJP proxy-tier RSS (avg / peak, summed) | 1080.80 MiB / 1158.60 MiB |
| PgBouncer nodes | N/A |
| PgBouncer server pool size per node | N/A |
| pgbouncer_reserve_pool_size | N/A |
| PgBouncer local HikariCP pool size per replica | N/A |
| HAProxy nodes | N/A |
| PgBouncer tier CPU (avg / peak, summed) | 139.60% / 833.20% |
| PgBouncer tier RSS (avg / peak, summed) | 1080.80 MiB / 1158.60 MiB |
| HAProxy CPU (avg / peak, summed) | N/A% / 0% |
| HAProxy RSS (avg / peak, summed) | N/A MiB / 0 MiB |
| Total PgBouncer proxy-tier CPU (avg / peak) | 139.60% / 833.20% |
| Total PgBouncer proxy-tier RSS (avg / peak) | 1080.80 MiB / 1158.60 MiB |

## Bench JVM System Metrics (in-process, median across instances)

| Metric | Value | Source |
|--------|-------|--------|
| **Bench JVM CPU (median)** | 8.70% | `OperatingSystemMXBean.getProcessCpuLoad()` |
| **Bench JVM GC pause total** | 34282 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 50 ms | ✅ PASS (44.17 ms) |
| Error rate | < 0.1% | ✅ PASS (0.0000) |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 5.195 | 25.295 | 201.343 | 115.94562056287681 | 0.005428001844367897 | 1.011807540492718 | 3903 |
| 1 | 18.607 | 71.103 | 232.191 | 141.98720507686363 | 0.004036673847288414 | 14.558662545116839 | 4639 |
| 2 | 4.703 | 20.735 | 204.287 | 111.11581014295245 | 0.005732939112720688 | 1.9650556485152295 | 3939 |
| 3 | 14.879 | 62.879 | 251.263 | 127.37157469951424 | 0.00438398655453877 | 14.353044965975926 | 4832 |
| 4 | 5.791 | 25.951 | 209.663 | 109.6585631909066 | 0.005498385252570871 | 0.421941045644908 | 3524 |
| 5 | 14.215 | 59.551 | 231.167 | 143.16735485661053 | 0.0040336550358822075 | 17.59735425389229 | 4481 |
| 6 | 5.827 | 28.815 | 199.167 | 146.39697675815646 | 0.004073259521748248 | 6.771242586909951 | 4124 |
| 7 | 13.823 | 59.039 | 237.183 | 136.4841139536189 | 0.0040465045180679456 | 12.946216533061541 | 4840 |

---

## Error Breakdown

| Instance | Error type | Count | First error message |
|----------|------------|-------|---------------------|
| 0 | other | 40 | — |
| 0 | sql_exception | 1561 | Unexpected error: Timeout waiting for admission control slot for operation: e7282124a6fbdd3c |
| 1 | other | 39 | — |
| 1 | sql_exception | 1417 | Unexpected error: Timeout waiting for admission control slot for operation: e7282124a6fbdd3c |
| 2 | other | 40 | — |
| 2 | sql_exception | 1581 | Unexpected error: Timeout waiting for admission control slot for operation: e7282124a6fbdd3c |
| 3 | other | 40 | — |
| 3 | sql_exception | 1379 | Unexpected error: Timeout waiting for admission control slot for operation: 51a40aebe7ec84e2 |
| 4 | other | 40 | — |
| 4 | sql_exception | 1494 | Unexpected error: Timeout waiting for admission control slot for operation: e7282124a6fbdd3c |
| 5 | other | 40 | — |
| 5 | sql_exception | 1427 | Unexpected error: Timeout waiting for admission control slot for operation: e7282124a6fbdd3c |
| 6 | other | 40 | — |
| 6 | sql_exception | 1475 | Unexpected error: Timeout waiting for admission control slot for operation: e7282124a6fbdd3c |
| 7 | other | 40 | — |
| 7 | sql_exception | 1363 | Unexpected error: Timeout waiting for admission control slot for operation: e7282124a6fbdd3c |
---
## OJP Proxy — JVM Heap and GC Metrics

> **Note:** Heap values are from `jstat -gc` (actual in-use JVM heap).
> OS RSS is **not** used here because the JVM does not return memory to the OS after GC.

| Proxy host | Heap used — median (MB) | Heap committed — median (MB) | Total GC time (s) | Young GC count | Full GC count |
|------------|------------------------|------------------------------|-------------------|----------------|---------------|
| ojp-1 | 37.0 | 77.0 | 2.650 | 1230 | 0 |
| ojp-2 | 36.0 | 63.0 | 9.559 | 5074 | 0 |
| ojp-3 | 30.9 | 53.0 | 11.564 | 4949 | 0 |
---
## PostgreSQL — Database Statistics

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 49 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 1560232 / 3377489 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 1741459259 | Cumulative since stats reset |
| Transactions rolled back | 0 | Non-zero → contention or application errors |
| Temp file bytes written | 1 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | 48 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 2532 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 269159 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> CPU% is normalised to a single core (100% = 1 CPU fully busy).
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | Avg CPU (%) | Peak CPU (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|-------------|--------------|---------------|----------------|
| Proxy (OJP / pgBouncer) | ojp-1 | 35.8 | 309.4 | 366.4 | 389.9 |
| Proxy (OJP / pgBouncer) | ojp-2 | 58.7 | 233.5 | 364.8 | 393.9 |
| Proxy (OJP / pgBouncer) | ojp-3 | 45.1 | 290.3 | 349.6 | 374.8 |
| PostgreSQL | db | 156.3 | 339.2 | 3822.1 | 4000.0 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-05-12T01:01:09Z*
