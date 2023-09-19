![image](https://user-images.githubusercontent.com/466385/220079388-e525fb2d-b69d-415c-8f36-165e4b73652d.png)

# Top Links
- [Blueprint Video on Sys Design](https://www.youtube.com/watch?v=o-k7h2G3Gco)
- [system-design-primer](https://github.com/donnemartin/system-design-primer)
- [grokking-the-system-design-interview](https://www.designgurus.io/course/grokking-the-system-design-interview)
- Blogs
  - [Blog on sys design](https://blog.pragmaticengineer.com/system-design-interview-an-insiders-guide-review/)
  - [Another blog on sys design in dev.to](https://dev.to/javinpaul/is-bytebytego-and-system-design-interview-an-insiders-guide-book-by-alex-xu-worth-it-266j)
  
# What is System design?
- a collection of technologies to serve a set of users to meet certain reqs.

# Components of system design
- Servers
- Applications
- Caches
- DBs
- Message queues
- Network Protocols

# Design Mantras
- FT-MLD
  - (F)unctional requirements
  - (T)echnical Reqs
    - design online system: is a blackbox + internally contain a collection of subsystems that may be geo	distributed + which interact with each other to expose an interface.
  - (M)icroservices
    - Arch diag joining the dots
    - Deep dive into each microservice
    - Scale each service : scale a.k.a. handle huge spurt in users without sacrificing response time
  - (L)ogical diagram
    - [Use draw.io](https://draw.io/)
    - [excalidraw](https://excalidraw.com/)
    - [draw.chat](https://draw.chat/)
    - [whimiscal](https://whimsical.com/)
    - Figma (what is suggested)
    - ![image](https://user-images.githubusercontent.com/466385/211135036-5b2e1ae5-5d52-4db7-8577-02c967b6426d.png)
  - Refs
    - https://gist.github.com/vasanthk/485d1c25737e8e72759f

# Evaluation Params

- Correctness
- Performance
  - Response Time : p99
  - Availability : five 9s
  - Throughput : 30k QPS

  - (D)eep Dive
- Non Func Requirements
  - CRUMPSS: Consistency Reliability Usability Maintainability Performance Security Scalability
    - Performance
      - Func req describe SLO for correctness
      - Non Func req describe SLO for availability | thoughput | response_time
      - SLI (indicator) : Correctness | Availability | Throughput | Response Time (p50, p99)
      - SLO (objective) : eg. p50 < 200ms p99 < 1s + availability >= 99.9%
      - SLA (agreement) : contract with endusers on what the SLOs are incl. consequences for miising the SLO( rebate | penalty)
- When to use a Distributed system | also applies to sharding
  - if need to scale DB | cache reqs dont fit in a single system
  - if high parallelization is needed i.e. large num of reqs / sec 
  - if latency is a factor due to geo factors 
  - for better SLA availability |reliability
  - for better tuning of hostpots
- Vert vs Horiz Scaling | ScaleUp vs ScaleOut
  - ScaleUp : more CPU|Mem|Disks|Network
    - simple to implement but does not always scale linearly wrt cost
    - has a limit to which it can be scaled up
# Framework
- Identify core prob
  - define user's view of the prob / end-user exp: may have multiple user personas
  - formulate functional requirement + optional func req
    - cluster func reqs into collection of microservices
    - draw arch diagram connecting the micro-services
    - if prob has only few microservices, dive into each and code
    - else decide which micro-service/s to touch upon by priority
  - to design MVP 
- algo that solves the prob
  - consider APIs - inputs and outputs
  - consider CAP
  - consider DB 
  - consider communication protocols  - REST, pull/push, msg broker, websockets... 
  - consider acceptance tests / test plan 
- implement algo as pgm
- convert pgm -> service
- build, then scale; scale the service for
  - increase in user traffic
  - capacity needs
  - computational needs
  - layer with SRLC - sharding / replication / load balancing / caching 
- wrap up
  - loadbalancer: RR|WRR|LeastConnections|Random
    - nginx|ELB|Citrix ADC|haproxy|Traefik|Seesaw
  - server
    - httpd|nginx
  - presentation layer : UI
    - angular|react|html
  - biz layer: application server logic + web service framework
    - python: flask|django|FastAPI
    - javascript: nodejs
    - java: tomcat|jetty
  - storage layer : DB
    - Relational: MySQL|PostGres|sqlite
    - NoSQL: Non relational DB
      - Obj Store:S3
      - Docbased: MongoDB|CouchDB|BerkleyDB|Cassandra
      - Key-value: Redis|AWSDynamoDB

# Simplification
- assume each server can handle 30k reqs/sec at 30% operating capacity. peak_capacity : 100k req/s
- assume 400 days / year
- assume 100k secs / day
- assume designing app for at least 3 yrs => 365*3 = ~1000 days
- assume each commodity server can have upto 12 cores, 128GB RAM and 2TB disk space
- Caching: 
  - assume caching 10% DB resuls in 90% cache hit rate
  - assume caching 20-30% DB resuls in 98-99% cache hit rate
  - app ...98-99% reads..> cache 20% 2Bill kvpairs
  - app ..........1-2% reads.....> DB (20TB | 10Bill kv pairs)
- For server CPU calculations
  - assume each server has about 8-12 cores, each core has 8 threads, so total 12*8 = ~100 threads pers commodity system
  - assume that each server is utilized 30-40%, so each system can spare 30 threads
  - assume each request takes x secs, so each thread can process 1000/x rps. 
  - 30/100 (cpu util) * 100(total_threads_in_a_commodity_server) * 1000/x(rps on a single thread) = 30000/x rps (req per sec).
    - app....>cache..........> DB 
      - app  :(x=1ms) : 30000rps
      - cache:(x=2ms) : 15000rps
      - DB   :(x=10ms):  3000rps
- when users grow use (SRLC) - sharding / replication / load balancing / caching 
  - for sharding, propose consistent hashing for almost all probs
  - for replication, consider workload nature and read-write replicas
  - 


# PEDALS
- Process requirement
  - Define goalpost, cust experience and acceptance tests
  - Whats Must-Have(key features), nice-to-have and out-of-scope
  - Non func requirements
- Estimate
  - Back of the envelope calculation abt servers, storage, mem and network bandwdith/latency
- Design the service
  - Key boxes : Servers, DB, 
- Articulate Data Model
  - DB schema, fields, 
- List Archi. Components
  - loadbalancer, read replicas, CDN, cache, backups, DR, HA, Upgrade
  - big picture, apis, happy path, non-happy path, s12y, security
  - tradeoffs in choices
  - Misc :Smoke/ Sanity / Jenkins
- Scale
  - Vertical (scale-up) / Horizontal (scale-out)
  - how to test scale

![image](https://user-images.githubusercontent.com/466385/203221706-85f48595-71c5-4ffa-810a-05e8f5162d84.png)
Ref: https://www.lewis-lin.com/blog/pedals-method

# Tables

## How many bytes make a ..?
2^..
- 20 Mill megs : 10^6
- 30 Bill gigs : 10^9
- 40 Trillion tubs : 10^12
- 50 Quadrillion (1000 trill) pubs : 10^15

## alternate mnemonic to remember pow(2)
- millionaire by 20
- billionaire by 30
- trillionaire by 40
- quadrillionaire by 50

![image](https://user-images.githubusercontent.com/466385/209053239-372ddb85-40d6-488d-b0ed-a161569813c3.png)

```
Number unit.       Mem unit.     Sci notation   Binary / logn base2
Thousand (K).      KB.                 10^3            2^10
Million (M).       MB.                 10^6            2^20
Billion (B).       GB.                 10^9            2^30
Trillion (T).      TB.                 10^12           2^40
Quadrillion.       PB.                 10^15           2^50  (1000 trillion)
```
# Further Reading on Mental math and back-of-the-envelope calculations
- https://www.maa.org/sites/default/files/doc/pubs/books/COSM_Chapter1.pdf
- https://ccnmtl.columbia.edu/projects/mmt/frontiers/web/ch2.html
- https://betterexplained.com/articles/mental-math-shortcuts/
- https://betterexplained.com/articles/how-to-develop-a-sense-of-scale/

## Time Complexity
- 1 < logn  < n  <  nlogn  < n2  < 2^n <  n! < n^n
- hash  binsrch  linear heapsort bubble fib     
```
O(1) = constant
O(log n) = logarithmic
O(n) = linear
O(n log n) = linearithmic
O(n^2) = quadratic
O(n^3) = cubic
O(2^n) = exponential
```

## Power of a modern PC
- a modern cpu can do about 100 mill basic math ops / sec => 10^2.10^6 = 10^8 ops /sec, each op takes ~10ns
- a supercomputer is about 10000 times faster than a single cpu => 10^12 ops/sec 

# How many ns in a sec
1 sec = 10^3ms = 10^9 ns (a bill. ns)
- nanosecond is time divided by 10^-9
- microsecond is time divided by 10^-6
- millisecond is time divided by 10^-3

# how many bits to represent ..
- Num # of bits needed to represent 'n' states =  [log2(n) + 1]
  -  1 bit to store 2 states
  -  2 bits to store 4 states
  -  4 bits to store 16 states
  -  8 bits to store 256 states
  - 15 bits to store 32768 states
  - 16 bits to store 65536 states
  - 30 bits to store 1 bill states
  - 32 bits to store 4 bill states

```
def gets_bits_to_store_states(states):
    return ceil( log2(states) )
```
![image](https://user-images.githubusercontent.com/466385/200450017-c506abd2-f619-4eb0-b286-1d9d7126231f.png)


# Uptime
## Availability Table - Cheat sheet
What you need to remember

| Availability level    | Downtime per year |
|-----------------------|-------------------|
| 90% ("one nine")      | 36.5 days         |
| 95%                   | 18.25 days        |
| 99% ("two-nines")     | 3.65 days         |
| 99.50%                | 1.83 days         |
| 99.9%("three nines")  | 8.76 hours        |
| 99.95%                | 4.38 hours        |
| 99.99%("four nines")  | 52.6 minutes      |
| 99.999%("five nines") | 5.26 minutes      |
| 99.9999%("six nines") | 31.5 secs         |
| 99.99999%("7 nines")  | 3.16 secs         |
| 99.999999%("8 9s")    |  315 ms           |
| 99.9999999%("9 9s")   |  31.5 ms          |


- https://gist.githubusercontent.com/dastergon/07751e9d3117ae0ead808cd39d4f92d1/raw/4515c0db813d45abf0ba2770123c26c311393ef7/availability-cheatsheet.md

| Availability level    | Downtime per year | Downtime per quarter | Downtime per month | Downtime per week | Downtime per day | Downtime per hour |
|-----------------------|-------------------|----------------------|--------------------|-------------------|------------------|-------------------|
| 90% ("one nine")      | 36.5 days         | 9 days               | 3 days             | 16.8 hours        | 2.4 hours        | 6 minutes         |
| 95%                   | 18.25 days        | 4.5 days             | 1.5 days           | 8.4 hours         | 1.2 hours        | 3 minutes         |
| 99% ("two-nines")     | 3.65 days         | 21.6 hours           | 7.2 hours          | 1.68 hours        | 14.4 minutes     | 36 seconds        |
| 99.50%                | 1.83 days         | 10.8 hours           | 3.6 hours          | 50.4 minutes      | 7.20 minutes     | 18 seconds        |
| 99.9%("three nines")  | 8.76 hours        | 2.16 hours           | 43.2 minutes       | 10.1 minutes      | 1.44 minutes     | 3.6 seconds       |
| 99.95%                | 4.38 hours        | 1.08 hours           | 21.6 minutes       | 5.04 minutes      | 43.2 seconds     | 1.8 seconds       |
| 99.99%("four nines")  | 52.6 minutes      | 12.96 minutes        | 4.32 minutes       | 60.5 seconds      | 8.64 seconds     | 0.36 seconds      |
| 99.999%("five nines") | 5.26 minutes      | 1.30 minutes         | 25.9 seconds       | 6.05 seconds      | 0.87 seconds     | 0.04 seconds      |

# Databases
## Choosing sql versus No-SQL databases
![image](https://user-images.githubusercontent.com/466385/202913528-7afdafc7-811e-43ea-af06-5b5d8f9c27e8.png)

### What is SQL DB?
- data has predefined schema
- Terminology: Tables|rows|columns|Joins
- Consistency has hipri vs Avalability | Perf

Eg. Oracle, PostGres, MySQL 
#### +ves
- when DB schema is known
- low latency compared to nosql
- Compliant with complex SQL DB queries and follows ACID properties and has Entity Relationshop model
- Has existed for ages; Great for accounting / legacy applications
- Scalability: Great for Vertical scaling / Scale-up Just add CPU/RAM/Disk 


#### -ves
- difficult to add a field
- difficult to shard

### What is NoSQL DB?
- Great for unstructured data and dynamic schema
- Data can be stored in many ways (document-oriented, column-oriented, graph-based or KeyValue based), follows CAP Properties
- Can tweak to prioritize Consistency | Availability | Perf
- Terminology: Mongo : Collection|documnet|field| embedded docs
Egs. 
Key-value: BerkleyDB, LevelDB, Redis, Cassandra, CouchDB, 
Col Oriented: Hadoop HBase
Doc Store:  Mongo (JSON BSON) YAMLDB (YAML)
Columnar DBs:
#### +ves
- great for semi-structured data like JSON/XML/CSV/Blobs
- Each doc can have its own structure
- can scale massively and can be sharded across nodes
- Scalability: Great for Horizontal scaling: Handle more traffic by sharding / adding more server nodes  
#### -ves
- difficult to do join operations across tables
- may result in duplication of data
- can result in inconsistency as NOSL does not support ACID transactions 

# Further Reading on system design articles
- https://gist.github.com/dastergon/dc9e3b89c4f251a047f617a9baadb5d8
- https://www.cs.rochester.edu/courses/261/fall2017/termpaper/submissions/06/Paper.pdf
- https://github.com/donnemartin/system-design-primer
- https://designgurus.org/blog/system-design-interview-basics-cap-vs-pacelc
- https://aaronice.gitbook.io/system-design/architecture-toolbox/latency-numbers
- https://bytebyte-go.s3.amazonaws.com/ByteByteGo_LinkedIn_PDF.pdf

# ACID Versus CAP
## ACID
### Atomicity
A transaction is an atomic unit of processing; it should
either be performed in its entirety or not performed at
all.
### Consistency preservation
A transaction should be consistency preserving, meaning
that if it is completely executed from beginning to end
without interference from other transactions, it should
take the database from one consistent state to another.
### Isolation
A transaction should appear as though it is being executed in iso- lation from other transactions, even though
many transactions are execut- ing concurrently. That is,
the execution of a transaction should not be interfered
with by any other transactions executing concurrently.
### Durability or permanency
The changes applied to the database by a com- mitted
transaction must persist in the database. These changes
must not be lost because of any failure

## CAP Theorem
For a distributed database, the CAP theorem states that it’s
impossible to simultaneously provide more than two out of
the following three guarantees:
### Consistency
Every read receives the most recent write or an error
### Availability
Every request receives a (non-error) response – without
guarantee that it contains the most recent write
### Partition tolerance
The system continues to operate despite an arbitrary
number of messages being dropped (or delayed) by the
network between nodes

![image](https://user-images.githubusercontent.com/466385/210057971-f72c8bef-8157-46b9-8187-7b250451e006.png)

## Summary
Based on CAP theorem, different database picks different
combination of consistency, avalability, and partition tolerence:
- CA: Relational Database
- CP, AP: Non-Relational Database

### Further Reading
- https://www.cs.rochester.edu/courses/261/fall2017/termpaper/submissions/06/Paper.pdf


# interesting stats to know
- Current active internet users : 5 Bill out of 8 bill ppl(Nov 2022) viz. 5x10^9 or 62% of world pop, adoption rate grows 4% annually(15 mill/mo).
- 65% of world pop has net access, more than 6 out of 10 ppl 
- 25% or1/4th of all net users in E.Asia, 17% in S.Asia and 10% in S.E Asia while Adrica has worlds fastest growing pop (126%)
- 4.3 bill mobile users with net | 54% of world pop, 50% world traffic comes through mobile
- avg person spends 7 mins daily on net 
- bit.ly
  - 2.3 bill links created / yr => 200mill shortlinks created/mo =>  200/30=6mill shortlinks/day => 72qps
  - 20 bill clicks/mo => (20x1000mill)/30 = 600 mill, shortlinks decoded/day => ~72*100links decoded/sec   
- Speed of light : 3.10^8m/s
- Speed (sound) : 340m/s

# RoundingOff
- memorize all powers of 2
  - 2^5=32
  - 2^6=64
  - 2^7=128
  - 2^9=512
  - 2^11=2048
  - ...   
- try to roundoff to nearest power of 2 or 10
- so 265 becomes 256 and 62 becomes 64
- https://www.youtube.com/watch?v=VBw703pjC3E
## QPS or RPS : Sizing
- https://dev.to/ievolved/how-i-calculate-capacity-for-systems-design-3477
### One Million tx a day means
- ~12 per sec
- ~700 per min
- ~4200 per hr

### One Million in Capacity
- https://avisri.medium.com/understanding-rules-of-thumb-for-computer-storage-e69797394cca

# Know your bottlenecks.
Just because you've determined your bandwidth can support 120/sec doesn't mean your entire system can. Parts of the system that might not be able to keep up:

- Database connections or throughput
- Hard disk reading/writing
- Utility that encrypts/decrypts data at high volumes
- Loadbalancer
- API call to 3rd party service that's rate throttled


# Qs
- Horizontal sharding vs Vertical sharding
  - https://en.wikipedia.org/wiki/Partition_(database)#Partitioning_methods
  - Horizontal, like cutting a layer cake side to side
    - diff rows in diff tables
    - north vs south, east vs west, where each zone has its own full stack
  - Vertical, like cutting a cake at a party
    - creating tables with fewer cols and using more tables to store remaining cols : called normalization
    - common form of vertical partitioning is to split static data from dynamic data, since the former is faster to access than the latter
    - where the dynamic data is not used as often as the static.
    
 
# Sample Probs
- URL Shortner
  - search + insert ops
  - In-mem Hash Index + shared log file(append only seq of records)

# how to time it
- Most system design interviews last for 45-60 minutes
- Interviewers generally want to see your high-level design within the first 20 minutes of the round.
- Breakup
  - First 10 mins: Ask clarifying qs
    - Mins 0-5: Clarify the scope of the question
    - Mins 5-8: Specify your assumptions
  - Mins 8-20: Design high-level 
    - 8-11: Calc metrics
    - 11-15: Identify high-level components or services
    - 15-20: Design the database
  - 20-45: Draw an architecture diagram
  - 30-35: Identify bottlenecks
  - 35-45: Dive into a specific component 
  - 45-60: Bring it all together
  - 45-55: Refine the architecture
  - 55-60: Questions for the interviewer

# Reference Links
- Intro to System Design: https://www.youtube.com/watch?v=FSR1s2b-l_I
 - [ByteByteGo Channel](https://www.youtube.com/watch?v=o-k7h2G3Gco)
 - https://igotanoffer.com/blogs/tech/system-design-interview-questions#:~:text=Keep%20in%20mind%20that%20interviewers,to%20allocate%20your%20time%20wisely
 - https://blog.tryexponent.com/how-to-nail-the-system-design-interview/
- How to generate ids on the cheap
  - https://code.flickr.net/2010/02/08/ticket-servers-distributed-unique-primary-keys-on-the-cheap/
  - https://betterprogramming.pub/uuid-generation-snowflake-identifiers-unique-2aed8b1771bc?gi=605a222fa212
- How to choose a DB
  - https://blog.bytebytego.com/p/ep36-types-of-databases-and-use-cases
  - https://towardsdatascience.com/choosing-the-right-database-in-a-system-design-interview-b8af9c6dc525?gi=0379cabc721e
- https://www.leanessays.com/
- [System Design Cheatsheet](https://gist.github.com/vasanthk/485d1c25737e8e72759f)
- [Interactive map] (https://colin-scott.github.io/personal_website/research/interactive_latency.html)
- https://aaronice.gitbook.io/system-design/system-design-systematic-approach
- https://www.educative.io/blog/complete-guide-to-system-design
- Sys design Courses
  - [ByteByteGo](https://bytebytego.com/buy?product=SystemDesignAnnualPass)
  - [Educative.io](https://www.educative.io/courses/grokking-modern-system-design-interview-for-engineers-managers)
  - [Udemy](https://www.udemy.com/course/system-design-interview-prep/)
  - [Exponent](https://www.tryexponent.com/courses/system-design-interview)  

# Mock Interviews
- https://interviewready.io/
- https://www.pramp.com/dashboard/
