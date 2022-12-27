# Useful algos to know for system design

- Merkle Tree
- Consistent Hashing
- Read Repair
- Gossip Protocol
- Bloom Filter
- Heartbeat
- CAP and PACELC Theorems


# Merkle Tree
- Used for identifying data inconsistencies between servers.
![image](https://user-images.githubusercontent.com/466385/209658228-966b0768-5655-4340-ad5e-9920c59abc64.png)

# Consistent Hashing
- Distributed systems use Consistent Hashing to distribute data across servers.
![image](https://user-images.githubusercontent.com/466385/209658291-73ee8b2a-b06e-4bdb-a759-8b809b68d696.png)

# Read Repair
- Read Repair is used to push the latest version of data to servers with older version.

# Gossip Protocol
- Used for efficiently sharing state information between servers.
- Each server keeps track of state information about other servers in the cluster and gossips (i.e., shares) info with a random server every second. 
- Eventually, each server gets to know about the state of every other node in the cluster.

# Bloom Filter
- Probabilistic data structure tells whether an element may be in a set, or definitely is not.
- only possible errors are false positives
- empty Bloom filter is a bit-array of m bits, all set to 0.
- There are also k different hash functions, each of which maps a set element to one of the m bit positions.

![image](https://user-images.githubusercontent.com/466385/209659085-db2a8ed5-aae9-40f7-9fab-61a86935f557.png)

# Heartbeat
- Mechanisms for detecting failures in a distributed system. Used for broadcasting the health status of a server.
- if exists a central server, all servers periodically send a heartbeat message to it. 
- If no central server, all servers randomly choose a set of servers and send them a heartbeat message every few secs.
- GFS and HDFS use Heartbeating to communicate with each other servers in the system

# CAP and PACELC Theorems
- We cannot avoid partition in a distributed system.
- So in the presence of a network partition, a distributed system should choose between consistency or availability.
-  ACID compliant DBs like RDBMSs like MySQL, Oracle, and MS-SQL Server, chose consistency (refuse response if it cannot check with peers).
-  In contrast, BASE (Basically Available, Soft-state, Eventually consistent) databases, such as NoSQL databases like MongoDB, Cassandra, and Redis, chose availability
    - (respond with local data without ensuring it is the latest with its peers).
- CAP theorem is silent is what happens when there is no network partition? What choices does a distributed system have when there is no partition?
- PACELC theorem states that in a system that replicates data:
  - if there is a partition (‘P’), a distributed system can tradeoff between availability and consistency (i.e., ‘A’ and ‘C’);
  - else (‘E’), when the system is running normally in the absence of partitions, 
    - the system can tradeoff between latency (‘L’) and consistency (‘C’).
  - (PAC) is the same as the CAP theorem, and the ELC is the extension. 
  - Examples
    - Dynamo and Cassandra are PA/EL systems: They choose availability over consistency when a partition occurs; otherwise, they choose lower latency.
    - MongoDB can be considered PA/EC (default configuration): MongoDB works in a primary/secondaries configuration. In the default configuration, all writes and reads are performed on the primary.
      - in the case of a network partition, MongoDB chooses availability.
      - Alternately, when MongoDB is configured to write on majority replicas and read from the primary, it could be categorized as PC/EC.   
    - BigTable and HBase are PC/EC systems: They will always choose consistency, giving up availability and lower latency.

![image](https://user-images.githubusercontent.com/466385/209659737-4003dc5d-75ba-4a07-8f35-c285285cb646.png)


# References
- https://levelup.gitconnected.com/7-algorithms-to-know-before-your-next-system-design-interview-d1de2f374ffa
- https://interviewnoodle.com/system-design-interview-basics-cap-vs-pacelc-cf7c5eebc313
