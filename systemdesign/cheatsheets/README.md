# Cheat Sheet

● Redundancy
  - Replication | Snapshot.
● High write load/storage
  - sharding | LSM trees Log-Structured Merge trees
● High read load - read replicas
● Scaling - Primary-Secondary or Leaderless
● High read/write concurrency - Duplicate record.
● Big objects - split into smaller chunks.
● Real time communication - Long polling / Websockets
● Search - index/primary key + reverse index
● Decoupling - message queues / pub-sub
● Hot spot elimination
  - Celebs in NewsFeed|SocialMedia|Twitter: hybrid push-pull
  - Peak time: Uber : surcharge|freemium models
  - Viral Video - Geo Hashing | Caching | CDN
- Back-of the envelope calculations needs dev to know
  - powers of 2
  - [availability](https://www.designgurus.io/blog/high-availability-system-design-basics) numbers :
    - https://www.enjoyalgorithms.com/blog/availability-system-design-concept
    - https://github.com/trohit/ik/blob/main/systemdesign/UPTIME.md
  - [latency numbers](https://gist.github.com/hellerbarde/2843375)  

# Approaches 
## educative.io
- RESHADED
  - Reqs + Esti + Stor + HLD + API + Details + Eval + Distinct feature
  - https://www.educative.io/blog/use-reshaded-for-system-design-interviews

# Refs 
- https://blog.bytebytego.com/archive
  - lots of them in https://www.linkedin.com/in/alexxubyte/recent-activity/images/ 
- https://securityzines.com/#zines
- https://matthewdbill.medium.com/back-of-envelope-calculations-cheat-sheet-d6758d276b05
- https://gist.github.com/mwakaba2/8ad25dda8c71fe529855994c70743733
- https://dev.to/ievolved/how-i-calculate-capacity-for-systems-design-3477
- https://itsallbinary.com/system-design-back-of-envelop-calculations-for-storage-size-bandwidth-traffic-etc-estimates/
- https://gist.github.com/vasanthk/485d1c25737e8e72759f
- https://igotanoffer.com/blogs/tech/latency-throughput-availability-system-design-interview


