# Why MsgQs?

- Allow Async | non-blocking
- retries to reach consumers,
- Better than Point-to-Point as it allows multiple consumers(say one for giving shortcode to consumer and another consumer for analytics)
- Pacing and independent scaling of producer and Consumer
- Can persist msgs if consumer is dead
- Both consumer and producer dont need to be alive at the same time
- Allow lock free data structures by consumers in some cases (say tinyurl allocations can be done without the shortcode allocation service needing to lock its data structures)
- All Msg qs use two common ways to handle messages: Queuing and Publish-Subscribe
- All Msg qs expect Consumer to either Push(MQTT Mosquitto/ HiveMQ) or Pull(Kafka)
  

# Usecases
- To send notifications to a consumer who may be offline (say new tweets / msgs / nearby friends / mails) whenever user comes online.
- Great for IoT and edge devices usecases that (may not be up all the time)
- For loose coupling a fat producer with many lightweight consumers that can say process only one request at a time and do so in a lock free manner.

# Examples
- RabbitMQ, Kafka, ActiveMQ
- Redis Streams, Pub.Sub : https://redis.com/solutions/use-cases/messaging/

# FAQ
- Difference between Msg Q and Task Q
- When would a push queue like this be preferable over a pull queue?
- Why is Kafka pull-based instead of push-based?
  - Scalability was the major driving factor also many consumers
  - https://stackoverflow.com/questions/39586635/why-is-kafka-pull-based-instead-of-push-based
   
  
## Kafka
- distributed messaging system that can reliably transfer a high throughput of messages between different entities.
  
# References
- https://www.youtube.com/watch?v=oVZtzZVe9Dg
- Notes: https://notebook.zohopublic.in/public/notes/u3i1s522a981ed32d48bcbb0b940ee3d58f22
- https://blog.scottlogic.com/2018/04/17/comparing-big-data-messaging.html
