```
Env	Suggestion
read heavy system	Cache
Need low latency	Cache + CDN
Need write heavy system	MsgQ for async processing
ACID compliance	SQL DB or RDBMS
If Data Unstructured or ACID not MUST	NO-SQL DB
Complex data in form of vid/img	Blob/Obj storage
if sys needs complex pre-processing like a newsfeed	MsgQ for async processing + Cache
If sys needs hisearch volume	index / tries / ElasticSearch
If need to scale SQL DB	Consider sharding
If sys needs HA + Perf + Throughput	Load balancer
If sys needs fast delivery globally + HA + perf	CDN
If sys needs to capture relationships like friend list/conns	Graph DB
Sys needs scaling of many components (db/server/etc)	Horizontal Scaling
If sys needs hi perf queries	DB Indexes
If sys needs bulk job processing	Batch processing + MsgQs
If sys needs reducing server load + DOS protection	Rate Limiter
If sys has microservices	API gateway for Auth/SSL/Termination/Routing)
If sys has single point of failure	Implement redundancy
If sys needs to be fault tolerant+durable	Data Replication
If sys needs bi-directional comms	Websockets
If sys needs to detect failures in a distributed sys	Heartbeats
If sys needs to ensure data integrity	Checksums
If sys needs to txfer data in decentralized way	Gossip protocol / Torrent
```
![image](https://github.com/user-attachments/assets/161bf6ce-f1dc-4c38-a13e-91e1c2b2cb54)
