![image](https://github.com/trohit/ik/assets/466385/043e4de2-a9bd-41ba-9bc1-c281c2d55216)
src: https://mattturck.com/bigdata2018/
latest:https://mattturck.com/mad2023/

# Distributed Filesystems for analytics
- Hadoop Distributed File System (HDFS):
  - Developed as part of the Apache Hadoop project.
  - Designed to store and manage large amounts of data reliably across commodity hardware.
  - Widely used in conjunction with Hadoop MapReduce/ Spark  for distributed processing.
  - Used alongwith Presto for analytics using SQL like queries
  - How HDFS works
    - has 2 kinds of nodes : NameNodes and DataNodes
    - DataNodes store data and NameNodes keep track of which DataNode stores what data
    - In case NameNode goes down, there is a secondary NameNode that takes over.
    - Each file is split into 128MB or 256MB chunks and then stored across various DataNodes
    - For redundancy and availability, at least 3 replicas of the data exist, in different nodes.
    - As HDFS has rack awareness, these replicas are stored in DataNodes across different racks.   
- Google File System (GFS):
  - Developed by Google as a proprietary file system for their internal use.
  - Served as an inspiration for HDFS and other distributed file systems.
  - Designed for high reliability, scalability, and efficient data processing.
- Amazon Simple Storage Service (S3):
  - Although not a traditional file system, it is a widely used object storage service provided by Amazon Web Services (AWS).
  - Popular for storing large amounts of unstructured data in a distributed and scalable manner.
- Ceph:
  - An open-source distributed storage system that provides object, block, and file storage in a single platform.
  - Known for its scalability, high performance, and ability to run on commodity hardware.
- GlusterFS:
  - An open-source, distributed file system that can scale horizontally.
  - It aggregates storage resources across nodes in a cluster to provide a single, unified namespace.
- Apache Cassandra:
  - Initially designed as a distributed NoSQL database, Cassandra also provides support for storing large amounts of data across a cluster.
  - Known for its high availability, fault tolerance, and linear scalability.

# SQL query engines for analytics
- Presto
- Spark
  - An open-source engine developed specifically for handling large-scale data processing and analytics
  - Spark allows users to access data from multiple sources including HDFS, OpenStack Swift, Amazon S3, and Cassandra.
  - Spark is significantly faster than Hadoop MapReduce because Spark processes data in the main memory of worker nodes and hence prevents unnecessary input/output operations with disks.
  - Spark is not a modified version of Hadoop and is not, really, dependent on Hadoop because it has its own cluster management. Hadoop is just one of the ways to implement Spark.
  - main feature of Spark is its in-memory cluster computing that increases the processing speed of an application.
  - Spark is designed to cover a wide range of workloads such as batch applications, iterative algorithms, interactive queries and streaming.
  - Why use Spark
    - Speed − Spark helps to run an application in Hadoop cluster, up to 100 times faster in memory, and 10 times faster when running on disk. This is possible by reducing number of read/write operations to disk. It stores the intermediate processing data in memory.
    - Supports multiple languages − Spark provides built-in APIs in Java, Scala, or Python. Therefore, you can write applications in different languages. Spark comes up with 80 high-level operators for interactive querying.
    - Advanced Analytics − Spark not only supports ‘Map’ and ‘reduce’. It also supports SQL queries, Streaming data, Machine learning (ML), and Graph algorithms.
  - Data Structure used by Spark
    - Resilient Distributed Datasets (RDD) is a fundamental data structure of Spark. RDD is an immutable distributed collection of objects.
    - Each dataset in RDD is divided into logical partitions, which may be computed on different nodes of the cluster.
    - RDDs can contain any type of Python, Java, or Scala objects, including user-defined classes. 
- Apache Hive
  - Apache Hive is a data warehouse infrastructure built on top of Hadoop and designed for querying and analyzing large datasets stored in Hadoop Distributed File System (HDFS) or other compatible distributed storage systems.
  - Hive provides a SQL-like query language called HiveQL, which allows users to express complex queries without needing to know Java or MapReduce.

# To learn
- https://brilliant.org/courses/data-analysis-fundamentals/
- https://www.udemy.com/topic/sql/free/
- https://www.coursera.org/professional-certificates/google-data-analytics
