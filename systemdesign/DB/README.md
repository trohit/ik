![image](https://user-images.githubusercontent.com/466385/209539804-77b9a653-8caa-4595-b6a0-617b9302b3ef.png)


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
Key-value: (in-mem)Redis|AWSDynamoDB
GraphDB : 
 - Neo4j|Arango|Azure CosmosDB
ColumnarDB: Amz RedShift| Apache Cassandra | Apache HBASE | Snowflake
Row-oriented DB: any classic sql DB
Time series DB: InfluxDB|RRDTool|Graphite|Prometheus

![image](https://user-images.githubusercontent.com/466385/215392835-49e70cac-7616-462e-9a83-72fb1d24a5f3.png)

![image](https://user-images.githubusercontent.com/466385/215309961-117777d0-14bd-4ca5-bf0e-9ddc21ff415d.png)


# Ref
- https://www.codekarle.com/system-design/Database-system-design.html
- https://towardsdatascience.com/choosing-the-right-database-in-a-system-design-interview-b8af9c6dc525
- https://stackoverflow.com/questions/14428069/sql-and-nosql-analogy-for-the-non-technical
- http://www.johndcook.com/blog/2009/07/06/brewer-cap-theorem-base/
