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
NoSQL: Non relational DB
Obj Store:S3
Docbased: MongoDB|CouchDB|BerkleyDB|Cassandra
Key-value: (in-mem)Redis|AWSDynamoDB

# Ref
- https://www.codekarle.com/system-design/Database-system-design.html
- https://towardsdatascience.com/choosing-the-right-database-in-a-system-design-interview-b8af9c6dc525
