# Conceptual
## Deadlocks
- a situation where a system that has more than one resource and more than one process cannot make progress due to being stuck in a loop.
- analogy: 2 vehicles on a narrow road
- https://stackoverflow.com/questions/61768299/can-a-single-process-thread-ever-cause-deadlock
  - try holding a semaphore twice in a recursive function
- Conditions for a deadlock: sys prone to deadlock if it has all the 4 conditions: MHNC
  - Mutual exclusion (exclusive access) 
  - Hold and wait (wait while hold) 
  - No pre-emption
  - Circular Wait
- Deadlock avoidance: https://www.geeksforgeeks.org/deadlock-prevention/
  - just avoid at least one of these 4 conditions
  - all processes to lock resources in a specific order aka give each resource a locking priority
  - yield resources and control + wait on a taskq (with callback) if resources are not present
   
# Whys
## Hashing
### Why do has functions use prime numbers ?
- primes are un-divisible by any other numbers. This includes 2 and this makes it odd too but the real reason, is its primeness
- https://computinglife.wordpress.com/2008/11/20/why-do-hash-functions-use-prime-numbers/
- In short: you can use nums like 17,31,397..

# Differences between

## Monolith vs Microservices arch
- in unix, there is a guiding rule that write a tool to do just one thing well and such that it can inter-operate or be invoked by other tool.
  - like cat scores.txt | sort | uniq -c   
- ### when to choose monolith
- for most designs that do not need scale monoliths work fine.
- Monolith also means you may need to pay the tech debt of refactoring later if you need large scale and a lerge number of independent components that interact with each other.

### when to use microservices
- guideline from a school of thought: a microservice should be deployable by not more than 2 devs working for a weeks worth of effort.  
- for most designs that operate at scale, microservices may be the answer.
- exceptions: maybe see amazon prime video
- when many technologies, DBs and teams are involved
  
## 2PL and 2PC
- 2 phase locking - for serializable isolation within a single database instance
- 2 phase commit - atomic commit across multiple nodes of a distributed database/datastores
- https://stackoverflow.com/questions/68640301/difference-between-2pc-2-phase-commit-and-2-pl-2-phase-locking
  
## CAP and PACELC
- CAP: In a network partition(P), one has to choose between (C)onsistency and (A)vailability.
- So in the presence of a network partition some systems, some designs choose CP (consistency-when-partitioned) or AP(availability-when-partitioned).
- Examples
  - CP: supports consistency and partition tolerance while sacrificing availability
    - eg. Most RDBMS like MySQL and PostgreSQL, also banking aplications
  - AP: supports availability and partition tolerance while sacrificing consistency
    - eg. Most NoSQL DBs like Cassandra, Riak, used for social media sites like insta|fb
 - PACLELC
   - Most of the time, there isnt a network partition. PACELC extends CAP to talk about these situations.
   - in case of network partitioning (P) in a distributed computer system, one has to choose between availability (A) and consistency (C) (as per the CAP theorem), but else (E), even when the system is running normally in the absence of partitions, one has to choose between latency (L) and loss of consistency (C).
   - Most NOSQL systems are PA/EL (available when partitioned, else choose latency)
   - except Mongo is PA/EC (availabile when partitioned, else choose consistency)
   - Most RDBMS are PC/EC

## Process vs Threads
[Process vs Threads](https://stackoverflow.com/questions/200469/what-is-the-difference-between-a-process-and-a-thread)

Per process items             | Per thread items
------------------------------|-----------------
Address space                 | Program counter
Global variables              | Registers
Open files                    | Stack
Child processes               | State
Pending alarms                |
Signals and signal handlers   |
Accounting information        |
- why use threads ?
  - creating a new process that *actually does work* is fairly expensive(creating a process involves the fork call, which is COW).
  - so threads are a lightweight construct, many threads belongs to a process. all threads write to a common shared mem owned by the process.
  - Threads may access and modify shared memory. Processes use inter-process communication instead.
- What are thread states
  - Runnable: A thread which is ready to run
  - Running: A thread which is executing is in running state.
  - Blocked: A blocked thread is waiting for a monitor lock is in this state. This thing can also happen when a thread performs an I/O operation and moves to the next state.
  - Waiting: It is a thread that is waiting for another thread to do the specific action.
  - Timed_waiting: It is a thread that is waiting for another thread to perform.
  - Terminated: A thread that has exited is in this state. 
- References
  - https://career.guru99.com/top-40-multithreading-interview-questions-and-answers/ 

## Differences between little endian(LSB) and Big Endian(MSB)
- https://stackoverflow.com/questions/22030657/little-endian-vs-big-endian
- https://betterexplained.com/articles/understanding-big-and-little-endian-byte-order/
## Diff between Redis vs Memcache
- Redis: in-mem key value store with a durable storage
  - https://redis.io/docs/get-started/faq/
  - needs just 3MB RAM to begin with
  - https://adevait.com/redis/what-is-redis
  - https://www.objectrocket.com/blog/how-to/top-5-redis-use-cases/
    - Session Cache, Leaderboard, Msg Qs, Persisted Counters,Pub/Sub, ...  
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

# Diff between Paxos vs Raft protocol

# Diff between 2PC vs 3PC
- Both are types of atomic committment protocols that work on distributed systems based on consensus used to commit transactions
- Involves a node that plays the role of a coordinator
- 2PC 2 phase committment protocol: different from 2PL (2 phase locking protocol : also called pessimistic concurrency control method)
  - Assumptions
    - stable storage at each node with a write-ahead log (WAL aka redo log) 
    - no node crashes forever
    - data in WAL is never lost|corrupted in a crash
    - any 2 nodes can communicate with each other
  - Workflow
    - 1st Phase: Commit request OR Voting Phase
      - "commit request" to all participants : blocking call that waits for reply or timeout
      - each node makes entry to their undo and redo|WAL log & replies with Ack|Goahead|YesVote.
      - in non-happy path, tx is aborted  
    - 2nd Phase: Do commit or completion phase
      - "do commit" request to all participants: blocking call that waits for reply|Ack from all participants
      - Each participant completes the operation, and releases all the locks and resources held during the transaction.
      - Each participant sends an acknowledgement to the coordinator.
      - The coordinator completes the transaction when all acknowledgements have been received.
      - In non-happy path (failure | timeout)
        - The coordinator sends a rollback message to all the participants.
        - Each participant undoes the transaction using the undo log, and releases the resources and locks held during the transaction.
        - Each participant sends an acknowledgement to the coordinator.
        - The coordinator undoes the transaction when all acknowledgements have been received. 
  - Cons
    - blocking protocol.
    - If after participant acking commit request, the coordinator fails permanently , some participants will never resolve their transactions.
      -  as participant will block until a commit or rollback is received
      - During the commit phase, a two-phase commit protocol cannot dependably recover from a failure of both the coordinator and a cohort member.
        -  If only the coordinator had failed, and no cohort members had received a commit message, it could safely be inferred that no commit had happened.
        -  If, however, both the coordinator and a cohort member failed, it is possible that the failed cohort member was the first to be notified, and had actually done the commit.
        -  Even if a new coordinator is selected, it cannot confidently proceed with the operation until it has received an agreement from all cohort members, and hence must block until all cohort members respond.
       
          
# Diff between Gossip protocol vs other alternatives

# Consistent Hashing vs other mechanisms
# Explain How your design will handle
## Concurrency Control
## Scalability
## Lockfree transactions
## Too many writes
## Too many reads

# HTTP
- [HTTP Codes](https://www.restapitutorial.com/httpstatuscodes.html)
- https://umbraco.com/knowledge-base/http-status-codes/
- https://developer.mozilla.org/en-US/docs/Web/HTTP/Status
- Imp HTTP codes
  - 100 continue, 101 Switching Protocols (Websocket), 200 success, 201 created, 202 job accepted, 301 perm redirect, 302 temp redirect,
  - 401 unauthorized, 404 not found, 405 method not allowed, 414 URI too long, 429 too many reqs,
  - 500 internal server err, 509 bandwidth exceeded,
 
# why cant I use 
## kafka as a Database
- kafka is meant for immutable writes so cant modify, cant do ACID transactions, cant index and search data, instead one should use a DB.
