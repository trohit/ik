![image](https://user-images.githubusercontent.com/466385/211182371-c323c453-e27d-4cb3-93c3-25f005e91a80.png)

# Time Mgmt : Phdsw
- Prob defn   :  5m 
- HLL         : 10m
- Deep Dive   : 10m
- Scalability : 10m
- Wrap-up     :  5m

# good questions to ask in any system design interview
- What are the specific functional requirements of the system? what is the main purpose ? What are the imp features ? multi-device support ?
- Who are our clients or consumers ? / Do we need to talk to existing peices of the system ? / What are the existing pieces ? 
- Can you elaborate on the non-functional requirements (e.g. performance, scalability, availability, consistency, latency, cost, security)?
  - focus on the most critical and reason it unless nudged in another direction.
- what is the daily traffic volume / whats the peak traffic QPS / 
- Are there any constraints or limitations we should consider?
- Can i assume that  / Is this a reasonable assumption / Do we need to consider / Do we need to log / monitor / store ? / can you give me a specific example
- what characters are allowed in the shortened url /  can urls be deleted or updated ?
- Is it a realtime system ? What are the supported devices ?
- What triggers notifications ? who triggers notifications ? will users be able to opt-out ? will recipients receive exactly one notification ?
- Do we need to consider security aspects like DDos detection / Cookie injection / CORS attack / end-to-end encryption ?
- Should we look into BCP and DR like Data loss due to DC down ?
- How many friends can a user have / How many tweets can a user post daily ? / Can feed contain images/vid/txt ?
- Will we support groups ? how long to store chat history ? should we support online presence ? 
- Is there a max msg size limit ? Is there any kind of throttling that we need to implement ? 

# Case Studies
Design
- TinyURL
- PasteBin
- Yelp
- NewsFeed
- Uber Clone
- Backend of a Dashboard to monitor many aplpication servers in a DC in realtime
- Recommendation system for Netflix
- LinkedIn | FB | Insta friends social feed
  - first |second | third degree of connection
  - firstDegree: O(1): since each users direct connections are in a set, simply do a lookup if 2ndDegreeUser in Users adj list : O(1)
  - secondDegree: O(n^2): A-B, A-C and B-C, so A-2nd-C. If any of A's friends are 1st degree friends of C, then A is 2nd degree friend of C
  - thirdDegree: O(n^3):  If any of A's friends are 2nd degree friends of C, then A is 3rd degree friend of C
- Streaming systems
![image](https://user-images.githubusercontent.com/466385/215305383-c6053834-e44b-44dc-b33c-583f0de20add.png)

- Video streaming
  - YoutTube|NetFlix|HotStar

# References
- 
