# Why MsgQs?

- Allow Async | non-blocking
- retries to reach consumers,
- Better than Point-to-Point as it allows multiple consumers(say one for giving shortcode to consumer and another consumer for analytics)
- Pacing and independent scaling of producer and Consumer
- Can persist msgs if consumer is dead
- Both consumer and producer dont need to be alive at the same time
- Allow lock free data structures by consumers in some cases (say tinyurl allocations can be done without the shortcode allocation service needing to lock its data structures)

- # Examples
- - RabbitMQ, Kafka, ActiveMQ
