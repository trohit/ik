# Some frequently used terms
- SEP: starburst enterprise platform
- Presto/ Trino/Starburst
- Stages of a Modern Data Warehouse
  - Ingest : the data 
  - Store : the data quickly in native forat
  - Transform : clean the data (databricks, Synapse serverless, Azure Data factory)
  - Model : copy the data into a format that more native to the end-user to use(like relational, start schema)
  - Visualize / ML : for the PowerBI user to create reports

# Data warehouse
- What: 
	- store data from multiple sources to act as a single src of truth. 
	- to be used for historical trend analysis and reporting
	- Not to be used by production apps
 - sometimes also called EDW (Enterprise Data Warehouse)
- Why
  - reduce stress on production system
  - optimized for red + sequential scans
  - integrate many sources of data
  - No IT involvement needed to create reports
  - One version of truth
  - Not affected by production system upgrades
  - Easy to create BI solns on top of it
  - can be used for anaytics without impacting production

# Data lake
- What 
  - schema on read repo that holds vast amt of raw data in native format until its needed
- Why
  - inexpensive to store data in native format
  - store data with no modeling
    
# Data Lakehouse 
- What
  - combines benefits of low cost storage and vast storage capacity of a data lake + the data structure and management capabilities of a data warehouse.
  - Think Apache Hadoop
# Data fabric
- Like a data Warehouse but adds more features 

# Storage Formats
- Why ?
  - 'cos trad formats like csv, XML, JSON, YAMl are too verbose and duplicate data
- Types of Formats
  - [ORC](https://en.wikipedia.org/wiki/Apache_ORC): Apache optimized row columnar format
    - Made in 2013 by FB and Hortonworks
    - used by most of the data processing frameworks Apache Spark, Apache Hive, Apache Flink and Apache Hadoop.
  - [Apache Parquet](https://en.wikipedia.org/wiki/Apache_Parquet):  free and open-source column-oriented data storage format in the Apache Hadoop ecosystem.
    - 2013: began as a joint effort between Twitter and Cloudera. Parquet was designed as an improvement on the Trevni columnar storage format created by Doug Cutting, the creator of Hadoop.
    - It is similar to RCFile and ORC, the other columnar-storage file formats in Hadoop, and is compatible with most of the data processing frameworks around Hadoop.
    - It provides efficient data compression and encoding schemes with enhanced performance to handle complex data in bulk.
    - Features
      - Col wise compression, encoding and compression techniques
      - col wise queries need not fetch entire column
      - bit packing, RLE
      - supports the big-data-processing frameworks including Apache Hive, Apache Drill, Apache Impala, Apache Crunch, Apache Pig, Cascading, Presto and Apache Spark. It is one of external data formats used by pandas Python data manipulation and analysis library
  - [Apache Thrift](https://en.wikipedia.org/wiki/Apache_Thrift) :  interface definition language and binary communication protocol used for defining and creating services for programming languages.
    - Developed by Facebook around 2007.
    - uses RPC + code gen to build cross-platform services.
    - includes complete stack for building clients and servers
    - has protocol and transport layers
    - Supported Protocols: Thrift supports a number of protocols : Binary | CompactBinary | JSON | SimpleJSON
    - Supported Transports: (SimpleFile | Framed | Memory | Socket | Zlib
    - Thrift also provides a # of servers: NonBlocking | Simple | Threaded | ThreadPool
  - gRPC
  - Apache Avro

 # Comparison
 ## Data Warehouse and Data Lakehouse
 - https://www.youtube.com/watch?v=VYmjJe2gR1A
 - Warehouse uses a Top-Down approach (what do I want and how do I get it ?)
   - Top Down
     - Understand corporate strategy
     - gather reqs (biz + tech)
     - impl. data warehouse (infra + ETL + Dimension model + reporting)
     - Create data sourced + Do analytics + BI 
 - Lakehouse uses a Bottom-up approach (what do I have and what can I make of it ?)
   - Bottom up
     - Ingest all data regardless of reqs
     - Store all data in native format without any schema defn
     - Do analysis and analytics (batch / interactive/ realtime/ machine learning / Data warehouse)
  ## Data warehouse and EDW (Enterprise Data warehouse)
  - EDW is a single repo for all of the org's data providing holistic understanding, consolidated data and easier data compliance.
