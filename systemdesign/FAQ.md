
# Differences between
## Diff between Redis vs Memcache
## Diff between Kafka vs RabbitMQ
- Kafka pull based means consumer responsible to keep asking Post Office "Do you have anything for me?"
  - In Kafka, if consumer goes down| n/w partition, an offset is maintained in every (broker + topic + partition) and same | another consumer can pick up from last offset
  - After some retries(need to clarify this bit), msg goes to dead letter q 
- In RMQ, broker itself will take responsibility to deliver msg to consumer
  - in RMQ, after few retries fail, msg goes to Dead letter Q.
- https://www.youtube.com/watch?v=oVZtzZVe9Dg
# Diff between socket|CPU|core
- https://stackoverflow.com/questions/40163095/what-is-socket-core-threads-cpu
- socket is the physical socket where CPU capsules are placed. A normal PC has just 1 socket.
- A socket can have multiple CPU Cores. A normal PC usually has 2-4 cores
- Some CPUs run more than one thread-per-core(think hyper-threading)
- CPUs = #_of_sockets * #_of_CPUs * #_of_Cores
- https://en.wikipedia.org/wiki/Simultaneous_multithreading
- https://blogs.vmware.com/customer-experience-and-success/2021/06/sockets-cpus-cores-and-threads-the-history-of-x86-processor-terms.html


# Diff between latency vs response time
`Latency + Processing Time = Response Time`
- where
- Latency = the time the message is in transit between two points (e.g. on the network, passing through gateways, etc.)
- Processing time = the time it takes for the message to be processed (e.g. translation between formats, enriched, or whatever)
- Response time = the sum of these.
  - eg. if 4 persons print a single sheet of paper at the same time and the printer takes 10s to print each sheet.
    - person1 whose print request is processed first  sees latency= 0s + processing_time=10s : so response time=10s
    - person4 whose print request is processed second sees latency=30s + processing_time=10s : so response time=40s

# Explain How your design will handle
## Concurrency Control
## Scalability
## Lockfree transactions
## Too many writes
## Too many reads

      
