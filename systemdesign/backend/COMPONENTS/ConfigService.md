# Examples
- Zookeeper, etcd, Chubby(distributed locking mechanism to provide dustributed locking, config, and coordination services to GFS and BigTable )

## Redis Distributed Lock Manager
- One cool thing about using [distributed locks in Redis cluster](https://redis.io/docs/manual/patterns/distributed-locks/) is that it doesnt overload the DB by depending on DB transactions and serialization.
- A good example is to [avoid double-booking in the TicketMaster example](https://www.hellointerview.com/learn/system-design/answer-keys/ticketmaster).
- Distributed locks need to take care of
  - Mutual exclusion
  - Deadlock
  - Fault Tolerance 

## Zookeeper
  - Distributed config and sync service
  - Used by Kafka prior to KIP-500 to store basic metadata about brokers, topics, partitions, partition leader/followers, consumer offsets, etc.
  - Kafka brokers are stateless; they rely on ZooKeeper to maintain and coordinate brokers, such as notifying consumers and producers of the arrival of a new broker or failure of an existing broker, as well as routing all requests to partition leaders.
  - In the older versions of Kafka, all clients (i.e., producers and consumers) used to directly talk to ZooKeeper to find the partition leader.
  - Kafka has moved away from this coupling, and in Kafka's latest releases, clients fetch metadata information from Kafka brokers directly; brokers talk to ZooKeeper to get the latest metadata.
## Chubby 
- Chubby is a service that provides a distributed locking mechanism and also stores small files. Internally, it is implemented as a key/value store that also provides a locking mechanism on each object stored in it. It is extensively used in various systems inside Google to provide storage and coordination services for systems like GFS and BigTable. Apache ZooKeeper is the open-source alternative to Chubby.
- Chubby is a CP system since all write go through the master. If a master dies, a backup is promoted to become the new master. Chubby continues to operate as long as more than half the nodes are up.
- In an election all nodes try to acquire the lock to become the master using Paxos. Only one suceeds.
- When a client wishes to use Chubby they ask the DNS that returns the ip of one of the Chubby nodes. Client then contacts the Chubby node via RPC, which redirects the client to the Master. Client then talks to the master.
- Chubby was developed to provide a reliable locking service. Over time other usecases developed:
  - Leader/master election: whichever node gets the lock first becomes the leader. similarly to elect a leader among multiple replicas
  - Naming service (like DNS):  DNS updates are usually cached, so delay before a mapping is effective. For fast updates, Chubby replaced DNS inside Google as a quick mechanism to discover servers. 
  - Storage (small objects that rarely change): Chubby provides a Unix like interface to store small files that dont change frequently. so Chubby used by GFS and BigTable to store metadata like ACLs 
  - Distributed locking mechanism (orig usecase)
    - Chubby provides coarse grained locks to sync activities in a distributed env.
    - in simple words chubby provides mutuxes and semaphores that work in a distributed env across nodes.
- Chubby uses Paxos as the distributed consensus protocol.
- Chubby also follows [TMR](https://en.wikipedia.org/wiki/Triple_modular_redundancy)
  - When not to use Chubby
    - Bulk updates | High data upload rate | Lock & unlock done very frequently | pub sub model
- Chubby locks are advisory, meaning its up to the client to honor the lock.
- Why chubby needs some storage ? for cliens to adverise the leader / secondary node, change  the binding of a name to IP. Not needing to have a separate set of servers for associated storage makes the workflow dependent on lesser discrete systems as well as little afster and easier to manage. As such Chubby only provides create, read,delete, and locking primitives.
- Example chubby path : ls/x/y/z/ab/c where
  - ls means lockservice
  - x is the name of the chubby cell usually a set of chubby server/s resolved via DNS lookup
  - a/b/c is a path within the Chuuby cell and is reolved locally within the cell itself
- Chubby uses seq_no to deal with msgs being recvd out-of-order.
- Each Chubby node can act as a Reader-writer lock by
  - if exclusive write lock then only one client maye hold the node
  - if shared read lock then any number of clients can hold the lock in read mode.
- Chubby vs Zookeeper
  - Similarities & Differences
![image](https://github.com/trohit/ik/assets/466385/cd00becd-f0fc-4f24-aca4-463753ff91ef)
![image](https://github.com/trohit/ik/assets/466385/9896b243-676c-4109-8514-248aeeb5429f)





- etcd
