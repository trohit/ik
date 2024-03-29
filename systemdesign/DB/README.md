![image](https://user-images.githubusercontent.com/466385/209539804-77b9a653-8caa-4595-b6a0-617b9302b3ef.png)
# References
1. [https://drive.google.com/drive/folders/1ChodcbMZ4KqS9WP9gin4sLVdCsgD3uoE] : [Jordanhasnolife](https://www.youtube.com/@jordanhasnolife5163/playlists)'s DB slide deck

# DB System design patterns
- Write ahead logging
- [Bloom filters](https://en.wikipedia.org/wiki/Bloom_filter)
  - APIs: Bloom filters have two operations:
    - add(x), which marks item x as an element of the set
    - is_member(x), which checks x’s membership in the set    
  - params
    - m total bits needed in bloom filter
    - n total items to store
    - k hash fns
    - p total proabililty of err
  - thumb rules
    - at p=0.1 or 1% false +ve, one needs 9.8 bits per elem key
    - at p=0.01 or 0.01% false +ve needs   
- Heartbeat
- Quorum
- Checksum
- Lease
- Split Brain
  
   
# DB Concepts
- In general, SQL DBs are optimized for more reads, not so much for writes. When you know the schema + queries you would run on them beforehand, RDBMS is a good choice.
- No SQL DBs are generally optimized for heavy writes, by default, do not work as well for a read heavy system.    
- BaSE : Basically available + Soft State + Eventual Consistency
  - Primarily used in: OLAP that needs high number of reads + maybe writes + scale
- ACID : Atomicity + Consistency + Isolation + Durability
  - Primarily used : OLTP + ACID
- Hybrid DBs
  - Where used: when you need some degree of OLTP/ACID + OLAP
    - eg. CockroachDB aims to provide whatever Postgres does (except triggers and stored procedures)
      - and also allow scaling while aiming for consistency and availability.
      - CockroachDB is a distributed SQL database that is designed to provide both consistency and availability, along with partition tolerance—the three key properties of the CAP theorem. The CAP theorem states that in a distributed system, it is impossible to simultaneously achieve all three of these properties. Here's how CockroachDB achieves consistency and availability
      - Scalability using Distributed Architecture + Consistent Hashing + Range Partitioning  + a form of Vector Clocks
      - Replication for High Availability
      - Consistent and Serializable Transactions using (Raft consensus algo + gossip protocol + Quorums for Reads and Writes )
        - gossip protocol for (node discovery + failure detection + cluster metadata propagation + anti-entropy & convergence
    - eg. TiDB (Titanium DB) aims to provide MySQL like features with scaling to meet both OLTP and OLAP needs
- How Databases store data
   - Generally older (1970s) DBs use B+Trees. Newer DB generally use LSM trees(1990s).
   - Thats not to say that LSM is bettter than the B+Trees. In general, B+Trees provide better read perf at the expense on write perf
   - DB's that use LSM trees provide better write / insertion perf over but are not as good as B+tree DBs at read perf.
      
![image](https://github.com/trohit/ik/assets/466385/49d750b4-c4d4-4c4e-bae3-f1b412ce3f5a)
src : [hellointerview:key tech](https://www.hellointerview.com/learn/system-design/in-a-hurry/key-technologies)

# How to choose SQL | NoSQL?
- If you prioritize low latency|scalability|wriiting large amt of unstructured data at the cost of consitency|atomcity => NoSQL
- If you prioritize consistency|atomicity|reading large amt of structured data => SQL
- If you are ok with scale-up/ vert scaling (=> SQL) but if you really want scale-out / horiz. scale (NoSQL)
- is your application schema and attrs and fields well defined (yes =>sql) ?
- Or is your application schema build-it-along-as-you-go ? (yes=> nosql) 
- what kind of queries would you be making? 
  - will it be limited to the doc (nosql) or
  - would you need lots of table wide joins (sql) ?
- Do you have a strong need for any of the foll. ACID (atomicity|consistency)?(yes>sql)  |isolation|durability
- Do you have a strong usecase for large scale and are willing to make a trade off b/w scale and go with eventual consistency ? (yes=>nosql)
- Would you rather have the DB manage the schema contraints ? (yes=>sql) OR
- Would you rather do many writes and have the application manage the consistency eventually ? (yes =>nosql)

# Analogy of SQL vs NoSQL
- SQL is like auto transmission which automatically selects the gear|torque vs NoSQL is like manual transmission which allows you fine grained control over the gears but at the expense of more overhead.
- if you are writing a recipe book and you want the ingredients and steps to be free flowing, (to be read by say a human) you'd  prefer NoSQL vs
- if the same recipe book were written for a robot that also orders fixed  ingredients as well as preset stored cooking procedures, then you can use enums for ingredients and procedures viz. SQL 

Relational DBs were the norm.
normalization in dbs were key to saving space
but new age data needs driven by data mining, pattrn analaysis resulted in an expolosion of attribs that needed to be stored calling for :
1. more volume of data
2. more velocity of consumption
3. more variety in the structure of how the data is stored anda represented viz. semi-structured or unstructured

trad dbs ended up needing sharding the data.
instead this data could be stored in a sigle document.

they were called nosql. but now these nosql dbs (key value stores + doc stores)  	also support a query lang and are often called new query lang dbs.
viz. cockroach db, google cloud spanner, yugabytedDB that support docs, sql + transactions.




storage layer : DB
Relational: MySQL|PostGres|sqlite
NoSQL: Not-only relational DB
Obj Store:S3
Docbased: MongoDB|CouchDB|BerkleyDB|Cassandra
Key-value: (in-mem)Redis|AWSDynamoDB|RocksDB
GraphDB : 
 - Neo4j|Arango|Azure CosmosDB
ColumnarDB: Amz RedShift| Apache Cassandra | Apache HBASE | Snowflake
Row-oriented DB: any classic sql DB
Time series DB: InfluxDB|RRDTool|Graphite|Prometheus

![image](https://user-images.githubusercontent.com/466385/224464870-ee1a169e-ddad-4cda-9f72-a523b77d2b35.png)

![image](https://user-images.githubusercontent.com/466385/215309961-117777d0-14bd-4ca5-bf0e-9ddc21ff415d.png)


# TradeOffs
- Scaling reads in RDBMS is hard; scaling writes in RDBMS is impossible [src slide#68](https://www.slideshare.net/jboner/scalability-availability-stability-patterns)

# Qs to ask

## Related to structure of data
- Do you have tables with lots of columns, only a few of which are actually used by any particular row?
- Do you have “attribute” tables where each row is a triple of (foreign key to row in another table, attribute name, attribute value) and you need ugly joins in your queries to deal with those tables?
- Have you given up on using columns for structured data, instead just serialising it (to JSON, YAML, XML or whatever) and dumping the string into your database?
- Does your schema have a large number of many-to-many join tables or tree-like structures (a foreign key that refers to a different row in the same table)?
- Do you find yourself frequently needing to make schema changes so that you can properly represent incoming data?

## relate to the scalability of your system:
- Are you reaching the limit of the write capacity of a single database server? (If read capacity is your problem, you should set up master-slave replication. Also make sure that you have first given your database the fattest hardware you can afford, you have optimised your queries, and your schema cannot easily be split into shards.)
- Is your amount of data greater than a single server can sensibly hold?
- Are your page loads being slowed down unacceptably by background batch processes overwhelming the database?

# Ref
- https://www.codekarle.com/system-design/Database-system-design.html
- https://towardsdatascience.com/choosing-the-right-database-in-a-system-design-interview-b8af9c6dc525
- https://stackoverflow.com/questions/14428069/sql-and-nosql-analogy-for-the-non-technical
- http://www.johndcook.com/blog/2009/07/06/brewer-cap-theorem-base/
- https://stackoverflow.blog/2021/01/14/have-the-tables-turned-on-nosql/

![image](https://github.com/trohit/ik/assets/466385/d485dc9a-0d01-415b-9b8a-0165c2842540)
src: https://www.youtube.com/watch?v=SxsMgHFNvWg

# Distributed Databases
- https://burcuku.github.io/cse2520-bigdata/dist-databases.html
- https://www.youtube.com/watch?v=6OFeuNy39Qg
- https://www.youtube.com/watch?v=UEAMfLPZZhE&list=PLeKd45zvjcDFUEv_ohr_HdUFe97RItdiB
- https://www.slideshare.net/andreimoga/cockroachdb

# Good Reading
- https://www.uber.com/en-SG/blog/postgres-to-mysql-migration/
- https://ottertune.com/blog/the-part-of-postgresql-we-hate-the-most

# ACID Transaction Isolation anomalies
- Of the four [ACID](https://en.wikipedia.org/wiki/ACID) properties in a DBMS (Database Management System), the [isolation](https://en.wikipedia.org/wiki/Isolation_(database_systems)) property is the one most often relaxed.
- Dirty Read: tx1 reads data that tx2 has not yet committed
- Non-repeatable read: tx1 reads same row twice but gets diff data each time cos tx2 does (UPDATE|DELETE + COMMIT). 
- Phantom read: tx1 reads data say set1 that matches some condition. tx2 then does UPDATE|INSERT based on o/p of tx1. tx1 then rexecutes stmt and gets a diff set set2.
- Refs
  - https://learn.microsoft.com/en-us/sql/odbc/reference/develop-app/transaction-isolation-levels?view=sql-server-ver16
  - https://stackoverflow.com/questions/43117231/non-repeatable-read-vs-phantom-read
  - non-repeatable read due to UPDATE but phantom due to INSERT|DELETE 
