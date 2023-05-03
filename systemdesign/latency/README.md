https://gist.github.com/jboner/2841832

# Whats is latency ?
- Latency is the time it takes for a packet to go from the sending endpoint to the receiving endpoint. 
- Many factors may affect the latency of a service. viz. QoS|CoS, jitter, processing delay, routing states, ..
- Latency is not explicitly equal to half of RTT, because delay may be asymmetrical between any two given endpoints.
- Reading
  - https://www.callstats.io/blog/what-is-round-trip-time-and-how-does-it-relate-to-network-latency
  

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
- cross VM Latency of two VMware guests on the same host :   20usec.
- latency between 2 EC2 instances in same AZ             :     < 100usec.
- RTT latency between 2 EC2 instance cross AZ            :              < 10ms (AZ's are within 60 miles / 100 kms of each other)
- Link latency between 2 sites for sync-rep              :              < 10ms  
  -  distance between systems should be under 100kms (~60 miles), due to the sync-rep distance limitation based on latency  
- Link latency between 2 sites across AWS regions        : [can vary widely](https://repost.aws/questions/QUl7IRSjpMQVe2mMOFojP6qA/a-question-about-inter-region-latency) [26ms(N.Virginia-Ohio) to 753ms(SPR-SaoPaolo)](https://www.concurrencylabs.com/blog/choose-your-aws-region-wisely/)
- Ref
  - https://www.xkyle.com/Measuring-AWS-Region-and-AZ-Latency/
  -  
# References
- https://computers-are-fast.github.io/
- https://www.youtube.com/watch?app=desktop&v=FqR5vESuKe0
- https://static.googleusercontent.com/media/sre.google/en//static/pdf/rule-of-thumb-latency-numbers-letter.pdf

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

