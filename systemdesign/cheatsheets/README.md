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
