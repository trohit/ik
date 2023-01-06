# What is sharding ?
- store data across multiple systems instead of just one
- reduces workload on any one single system
- ideal for distributed data stores
- usecases
  - to have highly scalale distributed id server (Snowflake by Twitter) 

# Why sharding ?
- modern web sites need fast access to an amount of information so large that it cannot be efficiently stored on a single computer. 
- A good way to deal with this problem is to "shard" that information; that is, store across multiple computers instead of on just one.

# Types of sharding
- Partitioning
   - (+) reduces storage needs of each system
   - (-) system still affected by hotspots 
   - Types of Partitioning
     - Horizontal 
     - Vertical 
- Replication
  - (+) increased availability and redundancy
  - (-) need for increased storage
  - (-) hard to be always consistent 
