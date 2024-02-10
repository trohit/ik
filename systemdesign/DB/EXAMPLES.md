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
- Write Consistency Levels: Any ..RF(Replication_factor).. All
  - Also can specify quorum within a DC(Local_quorum) and across DCs(Across_quorum)
  - Supports Hinted handoff
- Read consistency:
  - R+W>RF gives us strong consistency. In this equation R, W, RF are the read replica count, the write replica count, and the replication factor, respectively.
  - Snitch: The Snitch is an application that determines the proximity of nodes within the ring and also tells which nodes are faster. Cassandra nodes use this information to route read/write requests efficiently.
- Generation number: In Cassandra, each node stores a generation number which is incremented every time a node restarts. This generation number is included in each gossip message.
- The seed node designation has no purpose other than bootstrapping the gossip process for new nodes joining the cluster. Thus, seed nodes are not a single point of failure, nor do they have any other special purpose in cluster operations other than the bootstrapping of nodes.
- Cassandra Write path
  - Each write(create/update/delete) first appended to commit_log, then to in-mem memtable
  - Perodically, memtables flushed to SSTables which are in turn compacted periodically.
- Cache types:
  - Row cache: caches freq read rows
  - Key Cache: stores map (recently read partition keys -> SSTable offsets)
  - Chunk Cache: uncompressed chunks of data from SSTable thats read frequently
- Each SStable has a Bloom filter associated with it, which tells if a particular key is present in it or not. Bloom filters are used to boost the performance of read operations. These filters are stored in mem and are a special kind of key cache.
- Each SSTable has 2 files
  - Partition Index file:  stores the sorted partition keys mapped to their SSTable offsets.
  - Data file: stores actual data in sorted order.
- 
    

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
## Redis
- [Redis](https://db-engines.com/en/system/Redis) Remote dictionary server, written in C circa 2009
- A fast open src, distributed, in-mem key-value DB, cache & msg broker with optional [persistence & durability](https://redis.io/docs/management/persistence/)
- needs just 3MB to get started
- Redis is more than a cache. It is an in-memory data structure server. Has support for serialized [Transactions](https://redis.io/docs/interact/transactions/) and also Opportunistic Locking(using CAS|WATCH cmd) but does not support rollbacks for perf. 
- Widely used in places like Twitter, AirBnB, Yahoo and Amazon
- Supports many data types: Lists, sets, sortedSets, HasTables, and geohashing, PubSub
- Also supports JSON, XML, timeseries
- Persistence achieved by using either RDB (snaps) or AOF(append only file)
- Supports [master-replica](https://en.wikipedia.org/wiki/Replication_(computing)) (replication)[https://redis.io/docs/management/replication/]
- Can be used as cache, msgq, leaderboard, counter
- Often compared to Memcache which is only in-mem DB
- Best practices
  -  always recommended to keep shards to recommended sizes. General conservative rule of thumb is 25GB per process (or [50GB on Flash](https://redis.com/blog/redis-architecture-13-years-later/))  or 25K Ops/Second.
  -  With a large number of clients, a reconnect flood will be able to simply overwhelm a single threaded Redis process and force a failover. Hence, it is recommended that you should use a tool that allows you to reduce the number of open connections to your Redis server. eg. Redis Enterprise DMC proxy OR Twemproxy allows you to reduce the number of connections to your cache server by acting as a proxy.
  -  By default, Redis writes data to a file system at least every 2 seconds, with more or less robust options available if needed. In the case of a complete system failure on default settings, only a few seconds of data would be lost.
  - Data from any Redis server can replicate to any number of replicas. A replica may be a master to another replica. This allows Redis to implement a single-rooted replication tree.
  - Perf: Redis operates as a single process and is single-threaded or double-threaded when it rewrites the AOF (append-only file).
    - A Redis cluster can scale up to 1,000 nodes, achieve "acceptable" write safety and to continue operations when some nodes fail.
    - A single redis node can do about [200k+ TPS](https://stackoverflow.com/questions/35229274/can-redis-do-hundreds-of-transactions-per-second-on-single-key-value-pair) in production about 50K TPS(citation needed)
  - Scaling
    - [redis cluster can support upto 1000 nodes](https://medium.com/@inthujan/introduction-to-redis-redis-cluster-6c7760c8ebbc) supports in-built sharding and async replication   
- Refs
  - [Redis Antipatterns](https://developer.redis.com/howtos/antipatterns/)
  - Comparsion of [Redis vs DragonFly vs KeyTable vs SkyTable](https://news.ycombinator.com/item?id=31796311)

# TSDB
- Examples: OpenTSDB, InfluxDB, Prometheus(SoundCloud), Gorilla(FB), VictoriaMetrics
- 
# References
- https://db-engines.com/en/ranking
