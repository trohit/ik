# What is sharding ?
- is a fancy name for methods to partition data across systems 
- store data across multiple systems instead of just one
- reduces workload on any one single system
- ideal for distributed data stores
- usecases
  - to have highly scalale distributed id server (Snowflake by Twitter) 

# Why sharding ?
- modern web sites need fast access to an amount of information so large that it cannot be efficiently stored on a single computer. 
- A good way to deal with this problem is to "shard" that information; that is, store across multiple computers instead of on just one.

## When to think about sharding 
- when all the data doesnt fit on one system
- when the future size of the DB can become a perf bottleneck

## When not to do sharding ?
- if the DB size / scale of solution is too small to merit the sharding complexity
- when the data easily fits in one system
  - if you still want HA in such a system, just think of replication with read-replicas.

# Types of sharding
- Partitioning
   - (+) reduces storage needs of each system
   - (-) system still affected by hotspots 
   - Types of Partitioning
     - Horizontal : diff rows in diff tables
       - ![image](https://user-images.githubusercontent.com/466385/211133315-b3473026-1b96-4c76-947f-0c2389531bc8.png)
       - Examples
         - Consistent Hashing
         - Block Range Indexes:  provide similar benefits to horizontal partitioning or sharding but without needing to explicitly declare partitions
           - https://en.wikipedia.org/wiki/Block_Range_Index 
         - DB Sharding
           - HBase | CouchBase
           - Spanner, Google's global-scale distributed database, shards across multiple Paxos state machines to scale to "millions of machines across hundreds of data centers and trillions of database rows
           -    
     - Vertical : also called normalization, more tables with lesser cols viz. say split static data from dynamic data 
- Replication
  - (+) increased availability and redundancy
  - (-) need for increased storage
  - (-) hard to be always consistent 
  - Examples
    - Twitter used gizzard a middleware to replicate data across a distributed database to provide fault tolerance in the event of partitioning
      - gizzard is stateless middleware and provides eventual consistency
      - Gizzard is a middleware networking service that manages partitioning data + replication across arbitrary backend datastores (e.g., SQL databases, Lucene, etc.)
      - https://github.com/twitter-archive/gizzard 
      - Gizzard requires that all write operations be idempotent and commutative
      - Gizzard handles partitioning (i.e., dividing exclusive ranges of data across many hosts) by mappings ranges of data to particular shards.
      - These mappings are stored in a forwarding table that specifies lower-bound of a numerical range and what shard that data in that range belongs to.
      - Gizzard handles replication through a replication tree




![image](https://user-images.githubusercontent.com/466385/211129264-35bd830c-cf4d-40cf-80c1-5e36b51835eb.png)
![image](https://user-images.githubusercontent.com/466385/211129335-2a8b2a89-cb2c-4d37-a7d8-f1ca331376e0.png)


# Related
- https://en.wikipedia.org/wiki/Shard_(database_architecture)
- https://en.wikipedia.org/wiki/Partition_(database)
- https://technibbana.wordpress.com/tech/sharding-vs-consistent-hashing/
