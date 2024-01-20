# Prob
Popular social networks contain millions and even billions of connections between individuals.
Design a system that allows a user to search for another person, and see the shortest path between them.


# Goalpost
- a social n/w
- examples: fb / linkedin
- focus on the service that allows a user A to see the shortest path with another person B
- addon: share the image / media (url/text) with user B
- Userbase: 100m..1b DAU: 10%(Userbase) = 10m..100m
- 10m x 10 = 100m searches /daily
- QPS: 100^10^6 / 10^5 secs
= QPS: 10^3
- User A can add another user C as well

# NFR
- Available
- Low Latency, responsive
- Accurate
- Scalable


# Assumptions
- its a dynamically adding social n/w : User A adds 10 friends / week
- each User can have on avg 1000 friends
- user friends cap at 5000

# HLL

unique userid
user database:
NoSQL : Graph DB Neo4J / Cloud : AWS Neptune

user
  userid: int
  friends: [set]
  
 each user represented by a node 
 each node will have vertices to each of the users friends
 
 
 APIS
  find_relation: 
    param:
      src_userid
      dst_userid
    response: 
      [uA, u2,u3,...UB]
      
   
https://excalidraw.com/#room=56c0a763a37617cff251,Xj50BpkhdMblnHQcVf7mzw

 

  

# Diagram

![image](https://github.com/trohit/ik/assets/466385/ff5cacea-c3d8-4890-96fe-8121a32b5d4e)

# 
