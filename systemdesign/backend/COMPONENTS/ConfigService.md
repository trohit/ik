# Examples
- Zookeeper
  - Distributed config and sync service
  - Used by Kafka prior to KIP-500 to store basic metadata about brokers, topics, partitions, partition leader/followers, consumer offsets, etc.
  - Kafka brokers are stateless; they rely on ZooKeeper to maintain and coordinate brokers, such as notifying consumers and producers of the arrival of a new broker or failure of an existing broker, as well as routing all requests to partition leaders.
  - In the older versions of Kafka, all clients (i.e., producers and consumers) used to directly talk to ZooKeeper to find the partition leader.
  - Kafka has moved away from this coupling, and in Kafka's latest releases, clients fetch metadata information from Kafka brokers directly; brokers talk to ZooKeeper to get the latest metadata. 
- etcd
