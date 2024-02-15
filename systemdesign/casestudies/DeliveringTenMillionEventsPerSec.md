# Goal
- What system design pattern would we choose to deliver millions of  events to millions of subscribers with minimal latency ?

# FR
- ordering not imp
- p99.9 within 2 secs
- listeners only interested in certain subset of emitters
- must be scalable and fault tolerant
- within a DC
