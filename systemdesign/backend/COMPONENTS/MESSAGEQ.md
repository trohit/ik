# Why MsgQs?

- Allow loose coupling + buffering to an extent to deal with bursts as opposed to Rate limiting + allow independent scaling of producer and consumer
- Async | non-blocking
- retries to reach consumers,
- Better than Point-to-Point as it allows multiple consumers(say one for giving shortcode to consumer and another consumer for analytics)
- Pacing and independent scaling of producer and Consumer
- Can persist msgs if consumer is dead
- Both consumer and producer dont need to be alive at the same time
- Allow lock free data structures by consumers in some cases (say tinyurl allocations can be done without the shortcode allocation service needing to lock its data structures)
- All Msg qs use two common ways to handle messages: Queuing and Publish-Subscribe
- All Msg qs expect Consumer to either Push(MQTT Mosquitto/ HiveMQ) or Pull(Kafka) or both Push and Pull eg. RabbitMQ/ActiveMQ/Redis/Resque as brokers support both pull models ("get" in AMQP) and push models.
      
    
  

# Usecases
- To send notifications to a consumer who may be offline (say new tweets / msgs / nearby friends / mails) whenever user comes online.
- Great for IoT and edge devices usecases that (may not be up all the time)
- For loose coupling a fat producer with many lightweight consumers that can say process only one request at a time and do so in a lock free manner.

# Examples
- RabbitMQ, Kafka, ActiveMQ, 
- Redis Streams, Pub.Sub : https://redis.com/solutions/use-cases/messaging/

# FAQ
- Difference between Msg Q and Task Q (Celery) and JobQ (Resque)
  - essentially logs, msgs, alerts, tasks all the same to a MsgQ.
  - both message queues and task queues involve queuing mechanisms for managing workloads, only differ in usecase  
- When would a push queue like this be preferable over a pull queue?
  - When push is preferred ?   
    -  push queues are often preferred in scenarios where real-time processing, reduced latency, simplified consumer implementation, and scalability are important considerations. eg. MQTT in IoT like applications
    -  push queues are advantageous for applications where low latency is a critical requirement, such as instant messaging systems, high-frequency trading platforms, online gaming or real-time analytics.
  - When is pull model preferred ?
    -  pull model is preferred in scenarios where batch processing, variable processing times, resource constraints, message acknowledgment, and fine-grained control over message processing are important considerations.  
    - For batch processing where consumers need to process messages in large batches rather than immediately upon arrival.
    - Variable processing times: Pull queues are suitable when message processing times vary significantly among consumers. In a pull model, consumers can control the rate at which they pull messages from the queue based on their processing capacity and workload. This allows consumers to adapt to fluctuations in processing times without overwhelming the queue system with excessive pull requests.
    - Resource-constrained consumers: Pull queues are preferred when consumers have limited resources or cannot maintain persistent connections to the queue system. In a pull model, consumers only need to establish a connection to the queue system when they are ready to pull messages, reducing the overhead of maintaining persistent connections. This can be advantageous for resource-constrained environments such as edge devices or mobile applications.
    - Message acknowledgment: Pull queues are suitable for scenarios where message acknowledgment is required to ensure message delivery and processing reliability. (Think Banking and payments) In a pull model, consumers explicitly acknowledge messages after processing them, allowing the queue system to track message delivery and detect failures or processing errors. This can help ensure message reliability and fault tolerance in distributed systems.
- Why is Kafka pull-based instead of push-based?
  - Scalability was the major driving factor also many consumers
  - https://stackoverflow.com/questions/39586635/why-is-kafka-pull-based-instead-of-push-based
   
## Google PubSub
## AWS SNS/SQS/Kinesis
## Azure Web PubSub

## Kafka
- open src, pub-sub, durable, highly scalable distributed messaging system that can reliably transfer a high throughput of messages between different entities.
- Kafka can also be thought of as a distributed append-only WAL OR Commit log OR Transaction log that can persistently store a seq of records.
- written in Java, created at LinkedIn in 2010 for internal use
- Records are always appended at the end(Right) and read by the consumer/s from L->R. Records once inserted, cannot be deleted or modified.
- Kafka follows the principle of dumb broker and smart consumer. Kafka doesnt track what consumers are read. Consumers are allowed to read from any offset and are expected to poll / pull msgs. This also allows the consumers to join / disconnect the cluster at any point in time.  
- Kafka Usecases
  - Metrics, Log aggregation, Stream Processing, Commit Log, Website activity tracking for analytics and eventual product suggestions
- Kafka terminology
  - Broker(single kafka server), record(A record is a message or an event that gets stored in Kafka) , Publisher(writes msgs), Subscriber(reads & processes msgs), topics, partitions, offset, Leader(responsible for R+W in a partition, every partition has a Kafka broker as a Leader ), Follower(
    - a record aka msg aka event aka alert contains : Timestamp + Key(msgs with same key written to same partition) + Header + optional headers + value
    - topic: Topics are diff categories for messages to be published.
      - A consumer can subscribe to many topics.
      - A topic can have many subscribers. 
      - A topic can have multiple partitions of smaller sizes for better perf and scalability
        - A partition is just an ordered set of msgs. Placing each partition of a topic on a separate broker allows a topic to hold many more msgs than the capacity of a single server. 
        - Ordering is maintained at a per-partition lvl, not across the topic.
        - A topic can have multiple partitions in the same broker
        - Producers / Publishers can publish to any partition for a topic. Usually a Round Robin strategy is used.
      - Offset: Each msgs that enters a partition of a topic is assigned a uniq seq id called an offset.
        - Offset sequences are known only to each partition. To locate a msg, we need to know the Topic, partition and offset num. 
  - Messages in a topic can be read as often as needed, unlike classic messaging systems, messages are not deleted after consumption. Instead, Kafka retains messages for a configurable amount of time or until a storage size is exceeded.
- To ensure data consistency, the leader broker never returns (or exposes) messages which have not been replicated to a minimum set of ISRs.
- Brokers keep track of the high-water mark, which is the highest offset that all ISRs of a particular partition share. The leader exposes data only up to the high-water mark offset and propagates the high-water mark offset to all followers.
- The num of consumers cant exceed the num of partitions for a topic. If it does, one or more consumers will be idle until an existing consumer unsubscribes from the partition.
  - Number of consumers in a group = number of partitions: each consumer consumes one partition.
  - Number of consumers in a group > number of partitions: some consumers will be idle.
  - Number of consumers in a group < number of partitions: some consumers will consume more partitions than others.
-  producer goes through the following steps before publishing a message:
  -  The producer connects to any broker and asks for the leader of 'Partition 1'.
  -  The broker responds with the identification of the leader broker responsible for 'Partition 1'.
  -  The producer connects to the leader broker to publish the message.
-  A single broker in the Kafka Cluster is elected as the Cluster Controller. Its responsible for creating/deleting topic, adding partitions, assigning leaders to partitions and monitoring broker failures. CC also communicates partition leader election results to all brokers in the cluster.  
  - If a Cluster Controller dies, a new one gets elected. If n/w controller cant talk to other nodes (due to n/w partition or Garbage collection), its considered to be dead. If it comes back online later, but another node has taken its role, its said to be a zombie controller. This can cause a Split Brain.
  - Split brain is handled using a generation clock which is a a monotonically increasing number which indicates the election term. The old controller may have a epoch num of 1 whereas the new controller may have a epoch gen of 2. This epoch number is stored in ZooKeeper.
  - Producer delivery semantics
    - Async: Fire & Forget: producer doesnt wait for an ack from leader or any node. Can be used for usecases where its ok to drop some msgs like log collection.
    - Committed to Leader: leader stores the msg but responds without waiting for commit success from followers. producer waits only for ack from leader
    - Committed to Leader & Quorum : producer waits for ack from leader and quorum followers.
  - Consumer delivery semantics
    - At most once: msgs maybe lost but never redelivered. Can be used for usecases where its ok to drop some msgs like log collection
    - At least once: msgs never lost but may get redelivered. Can be used for usecases where msgs are idempodent 
    - Exactly once: msgs delivered exactly once. Can lead to decreased througput.
  - Kafka can provide high perf due to zero-copy from page cache -> n/w and sequential append only immutable writes and due to ability to chunk msgs together to  deliver large linear chunks to the user.
- Record retention: Kafka retains records till it runs out of disk space. Can set time-based limits(days, weeks, months) or size-based limits(M|G|T) or compaction (only keep the latest record).
- To prevent Monopolization of n/w and kafka server resources, kafka implements byte-rate thresholds defined per client-ID. A client-ID logically identifies an appl making a request. Multiple producer and consumer instances can share the sma client-ID. once the threshold is breached, say(10MB/s), broker does not return an err but instead slows down client by holding the clients response long enough to keep the lcinet under the quota. the adv here that client does not need to implement special backoff and retry behavior.
- Scalability
  - Kafka cluster can expand (add more brokers) or shrink(remove brokers) while in operation and without and=y outage.
  - Kafka topic can be expanded to include more partitions but is bounded by broker disk space.
  - no limit to how much data can be stored by a topic as once can increase num of partitions by increasing the num of brokers.
- Fault tolerance and reliability
  - broker failure detecable by zookeeper and other brokers
  - by using many consumer groups comsumption can have high throughput.
- Low latency : 99.9% of time, data served from RAM and cache and rarely hits the disk.    
- References
  - https://www.confluent.io/blog/publishing-apache-kafka-new-york-times/ 
  
# References
- https://www.youtube.com/watch?v=oVZtzZVe9Dg
- Notes: https://notebook.zohopublic.in/public/notes/u3i1s522a981ed32d48bcbb0b940ee3d58f22
- https://blog.scottlogic.com/2018/04/17/comparing-big-data-messaging.html
