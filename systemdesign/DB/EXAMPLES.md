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

## Dynamo
- https://www.cs.cornell.edu/courses/cs5414/2017fa/papers/dynamo.pdf
- Highly Available + Scalable + Decentralized + EVentually Consistent
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
