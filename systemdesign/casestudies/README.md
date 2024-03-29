- Who is going to use it?
- How are they going to use it?
- How many users are there?
- What does the system do?
- Are you looking for a hi-level overview or low level overview ?
- What are the inputs and outputs of the system?
- How much data do we expect to handle?
- How many requests per second do we expect?
- What is the expected read to write ratioimage](https://user-images.githubusercontent.com/466385/211182371-c323c453-e27d-4cb3-93c3-25f005e91a80.png)

# Time Mgmt : Phdsw
- Prob defn   :  5m 
- HLL         : 10m
- Deep Dive   : 10m
- Scalability : 10m
- Wrap-up     :  5m

# TipsNTricks
- Scale: Caching, LoadBalancing and ScaleOut
- ConcurrencyControl
  - Optimistic Concurrency Control:  [Serializable Snapshot Isolation](https://distributed-computing-musings.com/2022/02/transactions-serializable-snapshot-isolation/) 
  - Pessimistic Concurrency Control: 2PL
# References
- https://github.com/donnemartin/system-design-primer
- https://github.com/gitgik/distributed-system-design/
- https://github.com/arpitbbhayani/system-design-questions
- https://github.com/karanpratapsingh/system-design
- https://github.com/checkcheckzz/system-design-interview
- https://leetcode.com/discuss/interview-question/system-design/4485980/Navigating-Recent-System-Design-Assessments%3A-A-Candid-Reflection
- https://www.hellointerview.com/learn/system-design/in-a-hurry/introduction

# good questions to ask in any system design interview

- What are the specific functional requirements of the system? what is the main purpose ? What are the imp features ? multi-device support ?
- Who are our clients or consumers ? / Do we need to talk to existing peices of the system ? / What are the existing pieces ? 
- Can you elaborate on the non-functional requirements (e.g. performance, scalability, availability, consistency, latency, cost, security)?
  - focus on the most critical and reason it unless nudged in another direction.
- what is the daily traffic volume / whats the peak traffic QPS / 
- Are there any constraints or limitations we should consider?
- Can i assume that  / Is this a reasonable assumption / Do we need to consider / Do we need to log / monitor / store ? / can you give me a specific example
- what characters are allowed in the shortened url /  can urls be deleted or updated ?
- Is it a realtime system ? What are the supported devices ?
- What triggers notifications ? who triggers notifications ? will users be able to opt-out ? will recipients receive exactly one notification ?
- Do we need to consider security aspects like DDos detection / Cookie injection / CORS attack / end-to-end encryption ?
- Should we look into BCP and DR like Data loss due to DC down ?
- How many friends can a user have / How many tweets can a user post daily ? / Can feed contain images/vid/txt ?
- Will we support groups ? how long to store chat history ? should we support online presence ? 
- Is there a max msg size limit ? Is there any kind of throttling that we need to implement ? 

# What to use when and why
## Core Database
### Relational Databases : Joins, Indexes, 
- PGSQL/MySQL

### NoSQL 
- Why ? flexible schema, scalability using consistent hashing + sharding
- DynamoDB : austo scaling, active-active replication with single digit ms cross region read & write perf + 5 nines SLA + multi-region global DB, serverless 
- MongoDB
- ScyllaDB
- Cassandra

### Blob
- Why? durability + near infinite scalability + cost + security encrypt-at-rest, suited for workloads with high reads + writes + no/few modify + chunking for multi-part upload
- S3, Google Cloud Storage

### Search Optimized DB:
- Why ? inverted indexes + tokenization + stemming(storing words in root form : running can be stored as run) + fuzzy search + scaling(many nodes + sharding) 
- ElasticSearch + Lucene / Solr

## API Gateway 
- Why ?auth + load balancing + rate limiting
- nginx, HA Proxy

## Queues
- Why ?buffer for bursty traffic + decoupling + independent scaling + multiple consumers
- msg ordering + built-in retries (max_retries + delay_bet_retries) + deadletter qs + partition based scaling + back pressure
- Kafka
- SQS

## Streams
- Why ? multiple consumers + pub/sub + large amounts of processing
- Kafka, AWS Kinesis

## Distributed Locking
- Why ? transaction locks + ACID across distributed DB instances 
- locking mechanisms (enusring liveliness 
- Zookeeper, etcd, Redis Lock using RedLock

## Distributed Cache
- Why ? reduced latency + increased perf + reduced load on DB resulting in better scalability
- Cache can be at various layers
  - Client side: Browser, Buf cache
  - In the network: DNS, CDN
  - Server side: API gateway (nginx) , service (redis) + DB cache   
- Redis, Memcached

## CDN
- Why ?
- Akamai, Cloudfront, CloudFlare

## VectorDB
- Why? for usecases like searching similar voices, features, fingerprints, LLM
- PineCone FAISS

## Open src file formats
- Why ? cos trad formats like csv, XML, JSON, YAMl are too verbose and duplicate data
- Parquet
- Thrift
- Avro


# Case Studies
Design
- [TinyURL](https://docs.google.com/document/d/e/2PACX-1vTWxGs8gl4pCSBqzX75wfaOG4n87OytHOLDw7ttFVEBSaKtMN1CIiS-PwJAsh9dSTNLQpaKWNUDvokG/pub)
- PasteBin
- Yelp
- NewsFeed
- Uber Clone
- Backend of a Dashboard to monitor many aplpication servers in a DC in realtime
- Recommendation system for Netflix
- LinkedIn | FB | Insta friends social feed
  - first |second | third degree of connection
  - firstDegree: O(1): since each users direct connections are in a set, simply do a lookup if 2ndDegreeUser in Users adj list : O(1)
  - secondDegree: O(n^2): A-B, A-C and B-C, so A-2nd-C. If any of A's friends are 1st degree friends of C, then A is 2nd degree friend of C
  - thirdDegree: O(n^3):  If any of A's friends are 2nd degree friends of C, then A is 3rd degree friend of C
- Streaming systems
![image](https://user-images.githubusercontent.com/466385/215305383-c6053834-e44b-44dc-b33c-583f0de20add.png)

- Video streaming
  - YoutTube|NetFlix|HotStar

# Architectures
- Microservice arch: where each component is an independent microservice and uses SOA (service oriented architecture)
- Cmd Query responsibility segregation [CQRS](https://martinfowler.com/bliki/CQRS.html) : separate read and write DBs
- Layered (n-tier) architecture
- Event Driven Architecture : uses production/detection and consumption | reaction to events
  
![image](https://github.com/trohit/ik/assets/466385/3a06273c-5dc9-415e-b2fe-0098ee893d70)


