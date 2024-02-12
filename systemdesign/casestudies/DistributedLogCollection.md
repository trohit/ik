# Prob
- Design a system that can collect logs of various formats from different nodes and pipe it to a Centralized log analysis service.

Qs
- How will you handle if there are too many logs or a very high logging rate ?
  - Use a buffer like a msg q
  - Can we drop processing of some msgs ?
  - Can we ask the client to backoff by throttling by using kind of rate limiter ?
  - Kafka does silent and transparent  throttling by delaying response to the reqs until the  reqs are within the acceptable threshold / quota.
