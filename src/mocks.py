from datetime import datetime
from src.cli_types import ProcessStats, RequirementsResults


TEST_RESULTS = [
    "******************** Stress Settings ********************",
    "Command:",
    "  Type: write",
    "  Count: -1",
    "  Duration: 1 SECONDS",
    "  No Warmup: false",
    "  Consistency Level: LOCAL_ONE",
    "  Serial Consistency Level: SERIAL",
    "  Target Uncertainty: not applicable",
    "  Key Size (bytes): 10",
    "  Counter Increment Distibution: add=fixed(1)",
    "Rate:",
    "  Auto: false",
    "  Thread Count: 10",
    "  OpsPer Sec: 0",
    "Population:",
    "  Sequence: 1..1000000",
    "  Order: ARBITRARY",
    "  Wrap: true",
    "Insert:",
    "  Revisits: Uniform:  min=1,max=1000000",
    "  Visits: Fixed:  key=1",
    "  Row Population Ratio: Ratio: divisor=1.000000;delegate=Fixed:  key=1",
    "  Batch Type: not batching",
    "Columns:",
    "  Max Columns Per Key: 5",
    "  Column Names: [C0, C1, C2, C3, C4]",
    "  Comparator: AsciiType",
    "  Timestamp: null",
    "  Variable Column Count: false",
    "  Slice: false",
    "  Size Distribution: Fixed:  key=34",
    "  Count Distribution: Fixed:  key=5",
    "Errors:",
    "  Ignore: false",
    "  Tries: 10",
    "Log:",
    "  No Summary: false",
    "  No Settings: false",
    "  File: null",
    "  Interval Millis: 1000",
    "  Level: NORMAL",
    "Mode:",
    "  API: JAVA_DRIVER_NATIVE",
    "  Connection Style: CQL_PREPARED",
    "  CQL Version: CQL3",
    "  Protocol Version: V4",
    "  Username: null",
    "  Password: null",
    "  Auth Provide Class: null",
    "  Max Pending Per Connection: null",
    "  Connections Per Host: 8",
    "  Compression: NONE",
    "Node:",
    "  Nodes: [172.22.0.2]",
    "  Is White List: false",
    "  Datacenter: null",
    "  Rack: null",
    "Schema:",
    "  Keyspace: keyspace1",
    "  Replication Strategy: org.apache.cassandra.locator.NetworkTopologyStrategy",
    "  Replication Strategy Options: {replication_factor=1}",
    "  Storage Options: {}",
    "  Table Compression: null",
    "  Table Compaction Strategy: null",
    "  Table Compaction Strategy Options: {}",
    "Transport:",
    "  factory=org.apache.cassandra.thrift.TFramedTransportFactory; truststore=null; truststore-password=null; keystore=null; keystore-password=null; ssl-protocol=TLS; ssl-alg=SunX509; store-type=JKS; ssl-ciphers=TLS_RSA_WITH_AES_128_CBC_SHA,TLS_RSA_WITH_AES_256_CBC_SHA; ",
    "Port:",
    "  Native Port: 9042",
    "  Thrift Port: 9160",
    "  JMX Port: 7199",
    "Send To Daemon:",
    "  *not set*",
    "Graph:",
    "  File: null",
    "  Revision: unknown",
    "  Title: null",
    "  Operation: WRITE",
    "TokenRange:",
    "  Wrap: false",
    "  Split Factor: 1",
    "CloudConf:",
    "  File: null",
    "",
    "INFO  [main] 2024-09-10 23:51:42,064 GuavaCompatibility.java:204 - Detected Guava >= 19 in the classpath, using modern compatibility layer",
    "INFO  [main] 2024-09-10 23:51:42,077 Cluster.java:280 - DataStax Java driver 3.11.5.3 for Apache Cassandra",
    "INFO  [main] 2024-09-10 23:51:42,123 Native.java:113 - Could not load JNR C Library, native system calls through this library will not be available (set this logger level to DEBUG to see the full stack trace).",
    "INFO  [main] 2024-09-10 23:51:42,124 Clock.java:60 - Using java.lang.System clock to generate timestamps.",
    "===== Using optimized driver!!! =====",
    "INFO  [main] 2024-09-10 23:51:42,154 Cluster.java:195 - ===== Using optimized driver!!! =====",
    "INFO  [main] 2024-09-10 23:51:42,206 NettyUtil.java:84 - Detected shaded Netty classes in the classpath; native epoll transport will not work properly, defaulting to NIO.",
    "INFO  [main] 2024-09-10 23:51:42,534 RackAwareRoundRobinPolicy.java:128 - Using data-center name 'datacenter1' for RackAwareRoundRobinPolicy (if this is incorrect, please provide the correct datacenter name with RackAwareRoundRobinPolicy constructor)",
    "INFO  [main] 2024-09-10 23:51:42,534 RackAwareRoundRobinPolicy.java:136 - Using rack name 'rack1' for RackAwareRoundRobinPolicy (if this is incorrect, please provide the correct rack name with RackAwareRoundRobinPolicy constructor)",
    "INFO  [main] 2024-09-10 23:51:42,535 Cluster.java:1810 - New Cassandra host /172.22.0.2:9042 added",
    "Connected to cluster: , max pending requests per connection null, max connections per host 8",
    "Datatacenter: datacenter1; Host: /172.22.0.2; Rack: rack1",
    "INFO  [main] 2024-09-10 23:51:42,551 HostConnectionPool.java:200 - Using advanced port-based shard awareness with /172.22.0.2:9042",
    "WARN  [cluster1-nio-worker-7] 2024-09-10 23:51:42,588 RequestHandler.java:303 - Query '[0 bound values] CREATE KEYSPACE IF NOT EXISTS \"keyspace1\" WITH replication = {'class': 'org.apache.cassandra.locator.NetworkTopologyStrategy', 'replication_factor' : '1'} AND durable_writes = true;' generated server side warning(s): Using Replication Factor replication_factor=1 lower than the minimum_replication_factor_warn_threshold=3 is not recommended.",
    "Created keyspaces. Sleeping 1s for propagation.",
    "Sleeping 2s...",
    "Warming up WRITE with 50000 iterations...",
    "Failed to connect over JMX; not collecting these stats",
    "Running WRITE with 10 threads 1 seconds",
    "Failed to connect over JMX; not collecting these stats",
    "type       total ops,    op/s,    pk/s,   row/s,    mean,     med,     .95,     .99,    .999,     max,   time,   stderr, errors,  gc: #,  max ms,  sum ms,  sdv ms,      mb",
    "total,         21998,   21998,   21998,   21998,     0.3,     0.3,     0.5,     0.8,     1.9,     3.7,    1.0,  0.00000,      0,      0,       0,       0,       0,       0",
    "total,         31716,   32777,   32777,   32777,     0.3,     0.2,     0.5,     0.7,     8.6,     9.3,    1.3,  0.14876,      0,      0,       0,       0,       0,       0",
    "",
    "",
    "Results:",
    "Op rate                   :   24,463 op/s  [WRITE: 24,463 op/s]",
    "Partition rate            :   24,463 pk/s  [WRITE: 24,463 pk/s]",
    "Row rate                  :   24,463 row/s [WRITE: 24,463 row/s]",
    "Latency mean              :    0.3 ms [WRITE: 0.3 ms]",
    "Latency median            :    0.3 ms [WRITE: 0.3 ms]",
    "Latency 95th percentile   :    0.5 ms [WRITE: 0.5 ms]",
    "Latency 99th percentile   :    0.8 ms [WRITE: 0.8 ms]",
    "Latency 99.9th percentile :    2.7 ms [WRITE: 2.7 ms]",
    "Latency max               :    9.3 ms [WRITE: 9.3 ms]",
    "Total partitions          :     31,716 [WRITE: 31,716]",
    "Total errors              :          0 [WRITE: 0]",
    "Total GC count            : 0",
    "Total GC memory           : 0.000 KiB",
    "Total GC time             :    0.0 seconds",
    "Avg GC time               :    NaN ms",
    "StdDev GC time            :    0.0 ms",
    "Total operation time      : 00:00:01",
    "",
    "END",
    "",
]

REQUIREMENTS_RESULTS = RequirementsResults(
    number_stress_tests=1,
    process_stats=[
        ProcessStats(
            start_time=datetime.datetime(2024, 9, 11, 20, 23, 53, 580820),
            end_time=datetime.datetime(2024, 9, 11, 20, 24, 4, 395492),
            duration=datetime.timedelta(seconds=10, microseconds=814672),
        )
    ],
    op_rate_sum=20.671,
    latency_mean_average=0.4,
    latency_99th_percentile_average=0.8,
    latency_max_std_dev=0.2,
)
