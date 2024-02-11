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
- RabbitMQ, Kafka, ActiveMQ
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
   
  
## Kafka
- distributed messaging system that can reliably transfer a high throughput of messages between different entities.
  
# References
- https://www.youtube.com/watch?v=oVZtzZVe9Dg
- Notes: https://notebook.zohopublic.in/public/notes/u3i1s522a981ed32d48bcbb0b940ee3d58f22
- https://blog.scottlogic.com/2018/04/17/comparing-big-data-messaging.html
