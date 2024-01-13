# References
- http://highscalability.com/blog/2013/7/8/the-architecture-twitter-uses-to-deal-with-150m-active-users.html
- https://www.infoq.com/presentations/Twitter-Timeline-Scalability/
  - Tweet service: handles scale
  - Target SLA: latency 5 secs
  - in-mem timeline clusters that incl. push notifications
  - timeline types
    - user timeline: all tweets certain user has sent 
    - newsfeed : merge of all user timelines that user cares abt (followees + interests)
      - but strips out ack replies and DMs
    - Query Timeline aka search API
    - Push infra: for paid users 100 ms latency) called Firehose
    - 1 mill. socket concurrency
    - can subscribe for interesting search terms
    - Pull infra
      - ingest rate QPS:400k
      - TFE ..> fan out ..> massive replicated redis cluster key:user val:[list of tweets they posted]
      - once tweet comes in, query fan out service 'flock' that knows all followers & followees
      - workflow: user A tweets, fanout service pushes it to 20k followers user keys and adds them to their newsfeeds
        - also tracks attribs like retweet, etc.
        -  
# Nuances
- Fan-out-on-read vs Fan-out-on-write
  - For celebs like Elon, too many followers, not all active: so makes sense to pull based fan out / fan-out on read
  - For small # followers, can easily do push based fan-out, so fan out on write
      
Reqs
- timeline
- search

Prob
- DAU: 10^7
daily: 10^7x 20 tweets
- QPS: 
day: 10^5secs

10^7 x 20 / 10^5
= 20x10^2
= 2000 QPS

Assumption: 20% YoY

API
public

POST /post tweet
  param:user_id, msg_body
  
GET /GET tweet_info
  param: userid, last_n
  
GET /timeline
  param: userid

GET /search
  param:search_str, meta_type: [account|tags|text]


HLD
diagram


https://excalidraw.com/#room=22c4259fb778680ceb3c,z5QAyk19NE7JlpN6eyOp6A

Scalability

Wrapup


