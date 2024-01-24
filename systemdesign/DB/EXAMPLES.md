# SQL RDBMS

## Postgres
- started out as a successor to Ingres, called postgres or PostgreSQL
- SQL RDBMS
  

# NoSQL 
- not only SQL
- also called [BASE|https://stackoverflow.com/questions/3342497/explanation-of-base-terminology] Basically Available, Soft state, Eventual consistency

## Redis
- [Redis](https://db-engines.com/en/system/Redis) Remote dictionary server, written in C circa 2009
- A fast open src, distributed, in-mem key-value DB, cache & msg broker with optional [persistence & durability](https://redis.io/docs/management/persistence/)
- needs just 3MB to get started
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
- Refs
  - [Redis Antipatterns](https://developer.redis.com/howtos/antipatterns/)
  - Comparsion of [Redis vs DragonFly vs KeyTable vs SkyTable](https://news.ycombinator.com/item?id=31796311)

# TSDB
- Examples: OpenTSDB, InfluxDB, Prometheus(SoundCloud), Gorilla(FB), VictoriaMetrics
- 
# References
- https://db-engines.com/en/ranking
