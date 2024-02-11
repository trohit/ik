# Examples
- Zookeeper, etcd, Chubby(distributed locking mechanism to provide storagr and coordination services to GFS and BigTable )
## Zookeeper
  - Distributed config and sync service
  - Used by Kafka prior to KIP-500 to store basic metadata about brokers, topics, partitions, partition leader/followers, consumer offsets, etc.
  - Kafka brokers are stateless; they rely on ZooKeeper to maintain and coordinate brokers, such as notifying consumers and producers of the arrival of a new broker or failure of an existing broker, as well as routing all requests to partition leaders.
  - In the older versions of Kafka, all clients (i.e., producers and consumers) used to directly talk to ZooKeeper to find the partition leader.
  - Kafka has moved away from this coupling, and in Kafka's latest releases, clients fetch metadata information from Kafka brokers directly; brokers talk to ZooKeeper to get the latest metadata.
## Chubby 
- Chubby is a service that provides a distributed locking mechanism and also stores small files. Internally, it is implemented as a key/value store that also provides a locking mechanism on each object stored in it. It is extensively used in various systems inside Google to provide storage and coordination services for systems like GFS and BigTable. Apache ZooKeeper is the open-source alternative to Chubby.
- Chubby was developed to provide a reliable locking service. Over time other usecases developed:
  - Leader/master election
    - whichever node gets the lock first becomes the leader.
    - similarly to elect a leader among multiple replicas
  - Naming service (like DNS)
    - DNS updates are usually cached, so delay before a mapping is effective. For fast updates, Chubby replaced DNS inside Google as a quick mechanism to discover servers. 
  - Storage (small objects that rarely change)
    -  
  - Distributed locking mechanism (orig usecase)
- 




- etcd
