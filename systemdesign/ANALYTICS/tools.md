- Automated validation of data quality: [GX]() or [Great_expectations](https://legacy.docs.greatexpectations.io/en/latest/intro.html)
- Data Versioning: [DVC](https://dvc.org/), [Quilt](https://github.com/quiltdata/quilt) : versioned data portal for s3 on AWS
- Distributed SQL execution engine : ( Presto | Trino | Starburst ), ( Dremel | Drill | Impala | Dremio )
- Workflow management platform : Apache Airflow, Apache Oozie, Azkaban(batch workflow job scheduler created at LinkedIn to run Hadoop jobs.)


#  Tools
- Hive HMS: (HMS) is a service that stores metadata related to Apache Hive and other services, in a backend RDBMS, such as Derby, MySQL or PostgreSQL.
- Hive HMS  metastore can be shared by Impala, Spark, Hive, and other services.

# Companies
- Data analytics vendors that offer in-situ analysis of data across data sources
  - Open source: trino, presto, dremio
  - Commercial: Starburst, Dremio, DataBricks, data virtuality, IBM, ahana, denodo, TIBCO, Atscale
- DB
  - Teradata 
- [Cloudera](https://en.wikipedia.org/wiki/Cloudera):  American data lake software company
  - started in 2008 by G!, Y!, FB and Haddop engineer Doug Cutting.
  - initially offered free Hadoop and charged for consulting. later offered commercial hadoop.
  - 2018: Cloudera merged with Hortonworks
## Apache
- Apache Arrow
  - development platform for in-memory analytics. It contains a set of technologies that enable big data systems to process and move data fast. 
  - language-agnostic software framework for developing data analytics applications that process columnar data.  
  - language-independent columnar memory format for flat and hierarchical data, organized for efficient analytic operations on modern hardware like CPUs and GPUs.
  - The Arrow memory format also supports zero-copy reads for lightning-fast data access without serialization overhead.
  - Arrow's libraries implement the format and provide building blocks for a range of use cases, including high performance analytics.
- Apache Airavata : software framework for executing and managing computational jobs on distributed computing resources including local clusters, supercomputers, national grids, academic and commercial clouds.
- Apache Superset : open-source software application for data exploration and data visualization able to handle data at petabyte scale (big data).
- Apache Derby: Embeddable RDBMS for OLTP written in Java (with just 3.5MB mem footprint). Used as defacto DB engine by HMS(Hive Meta store)
- [Apache Iceberg](https://iceberg.apache.org/) : open-source high-performance format for huge analytic tables written in java and python made in 2017
  - brings the reliability and simplicity of SQL tables to big data. Started at netflix to support data correctness and ACID that wasnt supported by Hive.
  - making it possible for engines like Spark, Trino, Flink, Presto, Hive, Impala, StarRocks, Doris, and Pig to safely work with the same tables, at the same time.
  - Features : Expressive SQL, Full schema eveolution, hidden partitioning, time travel and rollback, compaction,
    - Full schema evolution: Iceberg schema updates are metadata changes, so no data files need to be rewritten to perform the update.
    - Schema evolution changes are independent and free of side-effects as data is never over-written
  - Vendors that support iceberg: CelerData, Cloudera, Dremio, IOMETE, Snowflake, Starburst, Tabular and AWS
# Data Sources
- Quilt : https://open.quiltdata.com/
- Google Open images dataset: https://storage.googleapis.com/openimages/
