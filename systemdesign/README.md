# Design Mantras
- FCAD
  - Functional requirements
  - Collection of microservices
  - Arch diag joining the dots
  - Deep dive into each microservice
- Non Func Requirements
  - RUMPSS: Reliability Usability Maintainability Performance Security Scalability
- When to use a Distributed system
  - if need to scale DB | cache reqs dont fit in a single system
  - if high parallelization is needed i.e. large num of reqs / sec 
  - if latency is a factor due to geo factors 
  - for better SLA availability |reliability
  - for better tuning of hostpots
  
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
- when users grow use srlc - sharding / replication / load balancing / caching 
  - for sharding, propose consistent hashing for almost all probs
  - for replication, consider workload nature and read-write replicas


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

```
Number unit.       Mem unit.     Sci notation   Binary / logn base2
Thousand (K).      KB.                 10^3            2^10
Million (M).       MB.                 10^6            2^20
Billion (B).       GB.                 10^9            2^30
Trillion (T).      TB.                 10^12           2^40
Quadrillion.       PB.                 10^15           2^50  (1000 trillion)
```


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

## Summary
Based on CAP theorem, different database picks different
combination of consistency, avalability, and partition tolerence:
- CA: Relational Database
- CP, AP: Non-Relational Database

### Further Reading
- https://www.cs.rochester.edu/courses/261/fall2017/termpaper/submissions/06/Paper.pdf


# interesting stats to know
- Current active internet users : 5 Bill out of .91 bill ppl viz. 5x10^9 or 62% of world pop, adotion rate grows 4% annually.
- 65% of world pop has net access, more than 6 out of 10 ppl 
- 25% or1/4th of all net users in E.Asia, 17% in S.Asia and 10% in S.E Asia while Adrica has worlds fastest growing pop (126%)
- 4.3 bill mobile users with net | 54% of world pop, 50% world traffic comes through mobile
- avg person spends 7 mins daily on net 


# Sizing
- https://dev.to/ievolved/how-i-calculate-capacity-for-systems-design-3477
## One Million in Scale
- ~42k per hour
- ~700 per minute
- ~12 per second

## One Million in Capacity


# Know your bottlenecks.
Just because you've determined your bandwidth can support 120/sec doesn't mean your entire system can. Parts of the system that might not be able to keep up:

- Database connections or throughput
- Hard disk reading/writing
- Utility that encrypts/decrypts data at high volumes
- Loadbalancer
- API call to 3rd party service that's rate throttled


# Sample Probs
- URL Shortner
  - search + insert ops
  - In-mem Hash Index + shared log file(append only seq of records)
