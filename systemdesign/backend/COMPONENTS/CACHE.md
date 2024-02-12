# Why need a cache
- For Performance, lower latency , for lesser load on the DB layer.
- Biz value: lower latency leads to better conversion rates

# Complexity
`there are two hard things in computer science: naming things and cache invalidation.`

# Diagrams
# Cache by position
- Client Side
- DNS Cache
- CDN Cache
- In-Mem Cache
- FS Cache
- DB Cache
- CPU Caches: L1/L2/L3 of which L1 and L2 are CPU specific and L3 is usually a shared CPU cache

# Types of Caches
## Cache aside : most widespread caching pattern
  - Diagram: ![image](https://github.com/trohit/ik/assets/466385/99499a97-08e0-480c-b841-199430bacd7d) 
  - examples:  
  - pros:simplest to implement
    - biggest advantage of using Cache-Aside is that anybody can read the code and understand its execution flow.
    - minimal cache provider responsibility: it just needs to be able to get and set values
    - straightforward migrations from a cache provider to another one if needed
  - cons:
    - code needs to handle the inconsistency gap between the cache and the datastore.
      - eg. app successfully updated cache but fails to update the datastore. So app needs to implement retries.
      - if retries fail, data inconsistency: b/w cache and datastore.
    - puts load on app as it needs to make 2 writes: 1 to cache + 1 to datastore  
- (Read|Write) (through|back aka behind) Cache: Write-Through & writeback moves the writing responsibility to the cache provider.
  - ![image](https://github.com/trohit/ik/assets/466385/f2d8b084-af36-4053-82bb-4caf6ed7817d)
  - read thru cache: ![image](https://github.com/trohit/ik/assets/466385/819620ea-ff52-4a28-9d1d-04bb3c1f59d2)
  - diff b/w write-thru vs write-behind:
    - in write thru cache->db is synchronous + blocking
    - in write back cache->db is done in async non-blocking fashion 
  - examples: most filesystems like WAFL, UFS(EMC) use write through  
  - pros: app code is now free of failure handling and retry logic.
  - cons: cache has additional responsibility and load to write to datastore. 
## Write around Cache
## Write Back|Behind Cache
  - Diagram: ![image](https://github.com/trohit/ik/assets/466385/ca867f6b-e057-47c9-9c5f-531483b2423a)
## Refresh Ahead

# Cache eviction policies
- Random
- FIFO
- LRU
- LFU
- MFU
- ARC
  
# When to use what
- By default use, Read thru & Write Thru cache whenever possible.
- If looking for a really simple solution to test perf improvements due to caching, start with Cache-Aside
- If perf considerations outweigh cache vs db consistency, use Write-Back.
- Refresh Ahead caching is useful if a large amount of freq accessed data gets updated frequently and consistency is imp. for the app usecase   


# Examples
## Redis
- Redis is a single threaded open-source, in-mem data structure (KVstore that can act as a cache+ DB + msg broker). Supports scale-out by [Redis Cluster](https://redis.io/docs/management/scaling/) and Redis [Enterprise](https://redis.com/redis-enterprise/technology/linear-scaling-redis-enterprise/) 
- written in C
- can have multiple instances of redis in the same server to leverage all the cores
- Has basic data types like Strings, Hash, List, Set, SortedSets(for range queries), bitmaps, HyperLogLog, geospatial indexes and streams.
  - Strings
`SET user:bob:email bob@example.com`
`SET user:bob:age 31`
  - Hash
`HSET user:bob email bob@example.com`
`HSET user:bob age 31
  - List
`
- supports expiry of values
- supports persistence thru RDB (RedisDB) and AOF(Append Only files)
- suports multiple cache eviction policies [LRU|LFU|Random|no-eviction](https://docs.redis.com/latest/rs/databases/memory-performance/eviction-policy/)
-   
## Memcached
- Refs
  - https://distributed-computing-musings.com/2022/03/paper-notes-scaling-memcache-at-facebook/
    
# References
- https://codeahoy.com/2017/08/11/caching-strategies-and-how-to-choose-the-right-one/
- https://hazelcast.com/blog/a-hitchhikers-guide-to-caching-patterns/
- https://medium.com/@mmoshikoo/cache-strategies-996e91c80303
- https://www.enjoyalgorithms.com/blog/refresh-ahead-caching-pattern
- https://mechanical-sympathy.blogspot.com/2013/02/cpu-cache-flushing-fallacy.html
- https://nickcraver.com/blog/2019/08/06/stack-overflow-how-we-do-app-caching/

# References
- https://redis.com/ebook/redis-in-action/
- https://university.redis.com/courses/
