
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
