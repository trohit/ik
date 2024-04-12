# Some frequently used terms
- SEP: starburst enterprise platform
- Presto/ Trino/Starburst
- 5 Stages of a Modern Data Warehouse (ISTMV)
  - Ingest : the data 
  - Store : the data quickly in native forat
  - Transform : clean the data (databricks, Synapse serverless, Azure Data factory)
  - Model : copy the data into a format that more native to the end-user to use(like relational, start schema)
  - Visualize / ML : for the PowerBI user to create reports
- Medallion Arch:tiers of enterprise data mgmt, pioneered by DataBricks, adopted by Microsoft for its new data platform 
  - bronze:  
  - silver:
  - gold:
- data lake: centralized repository that allows you to store all your structured and unstructured data at any scale.
  - data lakes are designed to store data in its raw format (the same format when the data comes from its source),
    - whether it’s structured data like relational databases
    - semi-structured data like JSON or XML files
    - or unstructured data like text documents, images, videos, and log files.
  - Pros: Flexibility and Scalability 
  - Cons: Generally lack the consistency and integrity needed for business reporting purposes.  
- Data lakehouse
  - Combines data lake and data warehouse together
  - Has both the scalability and flexibility provided by data lake, and analytical capability and integrity provided by data warehouse. 
 
# Reference Diagrams
![image](https://github.com/trohit/ik/assets/466385/7f7d17ed-ea28-498f-9aca-17098db193d4)
src: https://www.ibm.com/topics/data-warehouse

# Data warehouse
- What:
   - store data from multiple sources to act as a single src of truth. 
   - to be used for historical trend analysis and reporting
   - Not to be used by production apps
   - Uses ETL to extract, load and transform data to its destination 
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
- Used for : Data warehouse used for OLAP (ROLAP|MOLAP|HOLAP) | Data Mining and Reporting
- Constraints: limited by cost as the data grows over time

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
  - See more on [data lakehouse](https://www.ibm.com/topics/data-lakehouse)
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

# Data integration methods
- Types of data integration methods
- When to use what: ETL recommended for smaller data repos whereas ETL | CDC | DV |SDI  preferred for larger volumes of data 
 - ETL:
   - Extract: from a variety of sources such as:
     - SQL or NOSQL servers
     - CRM and ERP systems
     - Flat files
     - Email
     - Web pages
   - Transform : can involve
     - filtering | cleaning | de-duping | validating | authenticating | performing calculations | converting col names & currencies or other units of memsurement
     - auditing data for quality & compliance
     - removing or enctypting confidential data
     - formatting data into joined tables to meet the needs of the taget data warehouse. 
   - Load
     - mv staging_area/data target_data_warehouse/data
     - can involve full regresh or incremental data changes
     - usually for lerge orgs this load process is well-defined, batch-oriented and automated and takes place during off hours.
 - ELT :
   - diff bet ELT and ETL is that ELT directly copies or exports data from source to target without needing to load the extracted data into a staging location
   - ELT useful for hi-vol unstructured datasets
   - ELT ideal for big data mgmt since it doesnt need much upfront planning for data extraction and storage.
 - CDC
   - identifies and captures only the data thats xhnaged on the src to the target system.
   - can be used to reduce the E(extract) in ETL 
 - Data replication: useful for creating backups in data recovery
 - Data virtualization: uses s/w abstraction layer to create a unified, fully usable view of data, seen as an alternative to ETL, can also be used alongside ETL.
 - Stream data integration
   - continuously consumes streaming data in realtime for consumption and analysis by the target system.
   - SDI enables a data store for powering analytics, ML and realtime apps such as fraud detection, imprving cust UX,..

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
## ETL vs ELT
- ETL (Extract, Transform, Load) and ELT (Extract, Load, Transform).
- ETL: data is transformed into a predefined format, then gets loaded into target storage
- ELT:data is loaded into the destination, and gets transformed only when requested
