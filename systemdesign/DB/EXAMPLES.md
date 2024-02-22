# SQL RDBMS

## Postgres
- started out as a successor to Ingres, called postgres or PostgreSQL
- SQL RDBMS
- Perf
  - A stock Postgres Db can handle about 2000TPS(src:SystemDesignInterviews-2 Digital Wallet pg342), with tuning and connection pooling (like pgpool) usually [5k](https://www.ashnik.com/fine-tuning-postgres-to-achieve-5000-queries-per-second/) TPS.
  - if the postgres instance is local, can do [14kTPS](https://www.reddit.com/r/PostgreSQL/comments/o4xrhg/postgres_runs_with_14k_transactionssecond_locally/?rdt=37997) but PGSQL instances in production are rarely local. 
  

# NoSQL 
- not only SQL
- also called [BASE|https://stackoverflow.com/questions/3342497/explanation-of-base-terminology] Basically Available, Soft state, Eventual consistency

## Cassandra
- Cassandra is a distributed, scalable, decentralized, P2P, leaderless, eventually consistent(tunable consistency)  NOSQL database.
- Cassandra uses SSTables and memtables(like BigTable) and consistent hashing, Partitioning and replication like Dynamo(KV DB).
- Design patterns used in Cassandra
  - Consistent hashing, quorum, WAL, segmented log, gossip, generation num, Phi accrual failure detector, Bloom filters, hinted handoff, read repair  
- [Facebook constructed Cassandra](https://www.cs.umd.edu/~abadi/papers/abadi-pacelc.pdf) to power its Inbox Search feature.
-  Cassandra is a NoSQL database which means we cannot have joins between tables, there are no foreign keys, and while querying, we cannot add any column in the where clause other than the primary key. These constraints should be kept in mind before deciding to use Cassandra.
- Cassandra has tables, multiple tables across nodes can be grouped in a keyspace, and ma group of keyspaces for a cluster.
- Just like Dynamo, Cassandra uses consistent hashing for data partitioning. Cassandra uses Murmur3 as the consistent hashing function. 
- In Cassandra, the primary key uniquely identifies every row in the table.
  - A primary key is composed of:
    - Primary_key = partition_key(decides how data is stored across nodes) + clustering_key(decides how data is stored within a node)
    - eg. pin_code, cinema_hall_id OR country_id, state_id
  -  We can have multiple clustering keys; all columns listed after the partition key are called clustering columns.
    - Within a node data is orederd by clustering_key  (a clustering key can be made up of multiple columns)
  - All Cassandra nodes learn about the token assignments of other nodes through gossip protcol.
  - Any node can handle a request for any other node's range. The node receiving the request is called the coordinator, and any node can act in this role. If a key does not belong to the coordinator's range, it forwards the request to the replicas responsible for that range.
  - A client may connect to any node in the cluster to initiate a read or write query. This node is known as the coordinator node. The coordinator identifies the nodes responsible for the data that is being written or read and forwards the queries to them.
- Replication
  - Replication factor: how many replicas the system will have
  - Replication strategy : which nodes will be responsible for the replicas
  - Each keyspace in Cassandra can have a different replication factor.
- Write Consistency Levels:  One, Two, Three, Quorum, Local_quoram, Each_quorum (majority of the replicas in each datacenter must respond), and Any and ALL.
  - Also can specify quorum within a DC(Local_quorum) and across DCs(Across_quorum)
  - For strong consistency in Cassandra: R + W > RF where R=Read replica count, W write replica count and RF is the replication factor 
  - Coordinator node supports Hinted handoff when the node responsible for writes is down
- Read consistency: For read requests, Cassandra has the same consistency levels as that of write operations except Each_quorum.
  - R+W>RF gives us strong consistency. In this equation R, W, RF are the read replica count, the write replica count, and the replication factor, respectively.
  - Snitch: The Snitch is an application that determines the proximity of nodes within the ring and also tells which nodes are faster. Cassandra nodes use this information to route read/write requests efficiently. Snithc is used to determine each node's rack and DC.
- Generation number: In Cassandra, each node stores a generation number which is incremented every time a node restarts. This generation number is included in each gossip message.
- The seed node designation has no purpose other than bootstrapping the gossip process for new nodes joining the cluster. Thus, seed nodes are not a single point of failure, nor do they have any other special purpose in cluster operations other than the bootstrapping of nodes.
- Cassandra Write path
  - Each write(create/update/delete) first appended to commit_log, then to in-mem memtable
  - Perodically, memtables flushed to SSTables which are in turn compacted periodically.
- Cache types:
  - Row cache: caches freq read rows
  - Key Cache: stores map (recently read partition keys -> SSTable offsets)
  - Chunk Cache: uncompressed chunks of data from SSTable thats read frequently
- Each SStable has a Bloom filter associated with it, which tells if a particular key is present in it or not. Bloom filters are used to boost the performance of read operations and stored in mem. These filters are stored in mem and are a special kind of key cache.
- Each SSTable consist of mainly two files. Index file (Bloom filter & Key offset pairs) & Data file (actual columns data). 
  - Partition Index file:  stores the sorted partition keys mapped to their SSTable offsets. is accessed from disk.
  - Partition summary: in-mem data structure that stores the byte offsets in the Partition index for fast access.
  - Data file: stores actual data in sorted order.
- Tombstones are used to manage deletions. Its a marker to indicate that data has been deleted. When we delete some data in Cassandra, for a node that is down or unreachable, that node could miss a delete. Default expriry time for a tombstone is 10 days, to give the unavailable node time to recover
  - Tombstones make Cassandra writes efficient but take storage space instead of shrinking it. Tombstones are discarded during compaction except if the node resposible for the tombstone is unreachable(Check it?)
    
  


## MongoDB

## Dynamo
- https://www.cs.cornell.edu/courses/cs5414/2017fa/papers/dynamo.pdf
- Highly Available + Scalable + Decentralized + EVentually Consistent
- [Amazon originally designed Dynamo](https://www.cs.umd.edu/~abadi/papers/abadi-pacelc.pdf) to serve data to the core services in its e-commerce platform (for example, the shopping cart) 
- Dynamo(Scalable distributed KV store) is different from DynamoDB(Scalable NoSQL DB)
- Dynamo falls within the category of AP systems (i.e., available and partition tolerant) and is designed for high availability and partition tolerance at the expense of strong consistency.
- Dynamo provides the following ops
  - put(key, context, obj)
  - get(key) 
## RocksDB
- 
# TSDB
- Examples: OpenTSDB, InfluxDB, Prometheus(SoundCloud), Gorilla(FB), VictoriaMetrics
- 
# References
- https://db-engines.com/en/ranking
