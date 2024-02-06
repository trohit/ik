https://gist.github.com/jboner/2841832

![image](https://github.com/trohit/ik/assets/466385/c5b65f7b-ddd9-4e61-b796-bbf6a9be710c)
- src: [Alphasort:Case-sensitive parallel external sort](https://www.vldb.org/journal/VLDBJ4/P603.pdf)
- q : [SO:why-do-we-need-multiple-levels-of-cache-memory](https://superuser.com/questions/695632/why-do-we-need-multiple-levels-of-cache-memory)
- q2: [SO:is-the-cache-size-or-number-of-cores-more-important](https://superuser.com/questions/317771/is-the-cache-size-or-number-of-cores-more-important-when-weighing-cpu-performanc)
- q3: [SO:where-exactly-l1-l2-and-l3-caches-located](https://superuser.com/questions/196143/where-exactly-l1-l2-and-l3-caches-located-in-computer)
- q4:[ssd-vs-ram-whats-the-cost-durability-difference](https://superuser.com/questions/1253125/ssd-vs-ram-whats-the-cost-durability-difference-and-limitation-to-using-ssd-as)

# Whats is latency ?
- Latency is the time it takes for a packet to go from the sending endpoint to the receiving endpoint. 
- Many factors may affect the latency of a service. viz. QoS|CoS, jitter, processing delay, routing states, ..
- Latency is not explicitly equal to half of RTT, because delay may be asymmetrical between any two given endpoints.
- Reading
  - https://www.callstats.io/blog/what-is-round-trip-time-and-how-does-it-relate-to-network-latency
  
![image](https://github.com/trohit/ik/assets/466385/50d1c555-14a3-44c6-84c9-74a7b60d7e4d)
# Things to Note
- Register access is fastest (1x)
- RAM is upto 1000 times slower than cache (1000x) 
- SSD is 4-5 times slower than disk (5000x)
- access from neighboring peer Nodes DRAM in same DC can be 10 times slower than local SSD (50,000x)
- acesss from local HDD 20 times slower than local HDD (100,000x)
- In general there is an addl 1 ms round-trip delay time per 100 km (62 miles).
- Ref : https://nickcraver.com/blog/2019/08/06/stack-overflow-how-we-do-app-caching/
  - L1: 1.3ns
  - L2: 3.92ns (3x slower)
  - L3: 11.11ns (8.5x slower)
  - DDR4 RAM: 100ns (77x slower)
  - NVMe SSD: 120,000ns (92,307x slower)
  - SATA/SAS SSD: 400,000ns (307,692x slower)
  - Rotational HDD: 2–6ms (1,538,461x slower)
  - Microsoft Live Login: 12 redirects and 5s (3,846,153,846x slower, approximately)

# Stats
- [src](https://www.linkedin.com/posts/anubhav-dube-b02557236_latency-and-throughput-are-some-of-the-important-activity-7145373167509835776-Spmr)
- L1 cache ref: 1ns
- L2 cache ref: 5ns
- RAM ref: 100ns
- SSD ref: 100us (1000x slower than DRAM) [src](https://rocksdb.blogspot.com/2013/11/the-history-of-rocksdb.html)
- ping RTT in same DC : from 50us [src](https://rocksdb.blogspot.com/2013/11/the-history-of-rocksdb.html)
## Stats for ref in sys design
- Reading 1 MB from RAM: 250 μs (0.25 ms)
- Reading 1 MB from SSD: 1,000 μs (1 ms)
- Transfer 1 MB over Network: 10,000 μs (10 ms)
- Reading 1MB from HDD: 20,000 μs (20 ms)
- Inter-Continental Round Trip: 150,000 μs (150 ms)
# In relative terms
- 1x for Ram transfer
- 5x for SSD transfer
- 50x for n/w transfer
- 100x for HDD transfer
- 1000x for inter continental RTT

## diagram
![image](https://github.com/trohit/ik/assets/466385/7bce9b56-c34a-422b-a4ed-4fbf952572dd)

![image](https://github.com/trohit/ik/assets/466385/863ffb64-6779-4688-b731-3b0b37c89916)
src: https://www.youtube.com/watch?v=uHAfTty9UWY
in 2024, 1TB RAM costs ~10K USD

## Cloud network latency
- intra / within AZ latency:sub ms
- inter AZ latency: single digit ms
- inter region latency: varies
- [AWS latency chart](
https://www.cloudping.co/grid)

# Latency vs Throughout
Latency plays a pivotal role in determining the delay experienced by users when sending or receiving data across the network. On the other hand, throughput is instrumental in establishing the capacity for multiple users to simultaneously access the network.


# How long is a nanosec ?
- Grace Hopper explains 1 ns: https://www.youtube.com/watch?v=9eyFDBPk4Yw
  - 1ns ia billionth of a sec ...1/10^12secs or in 1ns, light travels 11.8inches in vacuum (or 0.3m)
  - in comparison, 1us is a millionth of a sec, or in 1us, light travels 984ft or 300m
  - in 1ms, light travels 3x10^5m or 300kms
  
  # Did you know ?
  - In 1ms(300m) py can do 68000 iters of an empty loop.
  - or py can do a max 100mill iters in 1sec.
  - every 1000kms can add 10ms in network latency src:https://www.igvita.com/2012/07/19/latency-the-new-web-performance-bottleneck/
    - For web browsing experience, it turns out that latency, not bandwidth, is likely the constraining factor
  
# Need to know

- 1 ns		  : access CPU registers / clock cycle of modern CPU / L1 cache access
- 10 ns  	  : L2 cache access / few expensive CPU instructions (branch mispredict penalty) ; 10x slower than L1 access
- 10^2 ns  	  : DRAM access ; 10x slower than L2 access
- 25x10^4 ns      : 1MB read from DRAM [src](https://www.softwareyoga.com/latency-numbers-everyone-should-know/) : 2500x slower than single byte DRAM access
-    10^6 ns      : 1MB seq read from SSD [src](https://www.softwareyoga.com/latency-numbers-everyone-should-know/) : ~100x slower than DRAM
-    10^6 ns      : LAN latency RTT
-  2x10^7 ns      : 1MB seq read from HDD : 20x slower than SSD
- 15x10^7 ns      : RTT of network pkt from USA<>Europe : ~10x slower than 1MB HDD read


## Other not so imp latencies
- 100-1000ns	: cost of sys call  / md5(64bit num) 
- 1-10us		  : context switching between threads / 64KB copy in DRAM
- 10-100us	  : web server like NGINX processes an HTTP request / DRAM 1MB read / read 8K SSD 
- 100-1000us	: write 8K page to SSD / GET op from memcache / redis
- 1-10ms	  	: intra zone / cross AZ RTT latency / HDD seek time 
- 10-100ms	  : RTT bet USEast<>USWest / RTT from USEast<>EU / DRAM 1GB read	/ bcrypt passwd / TLS handshake 
- 100-1000ms	: cross AZ latency / RTT USWest<>SPR / 1GB read from SSD
- 1s+   		: 1GB txfer within same region
`
- cross VM Latency of two VMware guests on the same host :   20usec.
- latency between 2 EC2 instances in same AZ             :     < 100usec.
- RTT latency between 2 EC2 instance cross AZ            :              < 10ms (AZ's are within 60 miles / 100 kms of each other)
- Link latency between 2 sites for sync-rep              :              < 10ms  
  -  distance between systems should be under 100kms (~60 miles), due to the sync-rep distance limitation based on latency  
- Link latency between 2 sites across AWS regions        : [can vary widely](https://repost.aws/questions/QUl7IRSjpMQVe2mMOFojP6qA/a-question-about-inter-region-latency) [26ms(N.Virginia-Ohio) to 753ms(SPR-SaoPaolo)](https://www.concurrencylabs.com/blog/choose-your-aws-region-wisely/)
- Ref
  - https://www.xkyle.com/Measuring-AWS-Region-and-AZ-Latency/
 
### Datacenter Latency
- Within a datacenter:
  - High bandwidth: 1-100Gbps interconnects
  - Low latency: < 1ms within rack, 1-5ms across
  - Little to no cost
- Between datacenters
  - Low bandwidth: 10Mbps-1Gbps
  - High latency: 50-150ms
  - $$$ for fiber

# References
- https://computers-are-fast.github.io/
- https://www.youtube.com/watch?app=desktop&v=FqR5vESuKe0
- https://static.googleusercontent.com/media/sre.google/en//static/pdf/rule-of-thumb-latency-numbers-letter.pdf
- https://hpbn.co/primer-on-latency-and-bandwidth/
- https://hpbn.co/primer-on-web-performance/#anatomy-of-a-modern-web-application

# cheatsheet
- L1 cache reference                           0.5 ns
- L2 cache reference                           7   ns                      14x L1 cache
- Main memory reference                      100   ns                      20x L2 cache, 200x L1 cache
- Compress 1K bytes with Zippy             1,000   ns        1 us
- Send 1K bytes over 1 Gbps network       10,000   ns       10 us
- Read 4K randomly from SSD*             100,000   ns      100 us          ~1GB/sec SSD
- Read 1 MB sequentially from SSD*     1,000,000   ns    1,000 us    1 ms  ~1GB/sec SSD, 4X memory
- Disk seek                           10,000,000   ns   10,000 us   10 ms  20x datacenter roundtrip
- Read 1 MB sequentially from disk    20,000,000   ns   20,000 us   20 ms  80x memory, 20X SSD
- Send packet CA->Netherlands->CA    150,000,000   ns  150,000 us  150 ms

![image](https://user-images.githubusercontent.com/466385/210059563-b5f7245e-9252-4809-a19f-cf4945a9836b.png)


# from bytebytego

![image](https://user-images.githubusercontent.com/466385/211181052-98e1eae3-e558-41a0-b028-6d9007048e8e.png)

![image](https://user-images.githubusercontent.com/466385/211181070-02f39787-accf-4402-a0b6-e340bebeeeaf.png)

![image](https://user-images.githubusercontent.com/466385/211181089-c7dff97f-ba58-45e0-b733-ef9a3a73e72d.png)

![image](https://user-images.githubusercontent.com/466385/211182538-6ead502b-dc16-4398-817a-f79f99795f56.png)

