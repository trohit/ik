# Intro
- https://en.wikipedia.org/wiki/Comparison_of_data-serialization_formats
- Also called data storage format.

# Examples
- ORC(Optimized Row Columnar) format
  - developed in 2013 by FB and Hortonworks 
- [Apache Parquet](https://en.wikipedia.org/wiki/Apache_Parquet):  free and open-source column-oriented data storage format in the Apache Hadoop ecosystem.
  - It is similar to RCFile and ORC, the other columnar-storage file formats in Hadoop, and is compatible with most of the data processing frameworks around Hadoop.
  - It provides efficient data compression and encoding schemes with enhanced performance to handle complex data in bulk.
  - began as a joint effort between Twitter and Cloudera. Parquet was designed as an improvement on the Trevni columnar storage format created by Doug Cutting, the creator of Hadoop.
  - Features
    - Col wise compression, encoding and compression techniques
    - col wise queries need not fetch entire column
    - bit packing, RLE
    - supports the big-data-processing frameworks including Apache Hive, Apache Drill, Apache Impala, Apache Crunch, Apache Pig, Cascading, Presto and Apache Spark. It is one of external data formats used by pandas Python data manipulation and analysis library
- [Apache Thrift](https://en.wikipedia.org/wiki/Apache_Thrift) :  interface definition language and binary communication protocol[2] used for defining and creating services for programming languages.[3] It was developed by Facebook.
- gRPC
- Apache Avro
