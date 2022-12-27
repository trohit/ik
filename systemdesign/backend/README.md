# DO YOU KNOW HOW MUCH YOUR COMPUTER CAN DO IN A SECOND?
- On a new laptop with a fast SSD and a sketchy network connection
  - a simple py empty loop can do over 50mill iters/sec => (50,000,000 iters/sec)
  - an equiv loop in C compiled with gcc -O2 will do 10x of py => thats 500mill(500,000,000) iters/sec.
  - So how many empty iters in py in 1ms? (1/10^3sec)
    - ~50,000 iters/ms(to be exact 68000)
  - How many entries can we add in py to a dict in 1sec?
    - ~10 mill entries/sec(10,000,000 entries/sec)

# Network  
  - How many HTTP requests can be served off a single threaded py server ?
    - ~25000 QPS
    - so each request takes :
      - =   1 sec / 25x10^3 reqs
      - = 10^3 ms / 25x10^3 reqs
      - = 10^6 us / 25x10^3 reqs 
      - = 10^2 x 10 us/ 25
      - =    4 x 10 us
      - =    40 us
  - How many times can we download google.com in a second?
    - 4 / sec
  - How many times can we start the Python interpreter in a second?
    - ~60 /sec (exact 77)
    - assuming ~100 /sec each invocation of py takes 10ms ( 1000 ms / 100 py invocations )
   
# Storage
- SSD
  - How many bytes can we write to an output file in a second? # Note: we make sure everything is sync'd to disk before exiting :)
    - A typical SSD write speed is between 200-500MB/sec
    - Exactly 342,000,000 bytes/sec
- Memory
  - How many bytes can we write to a string in memory in a second?
    - DRAM write speed : 20-40GB/s
    - will guess 10GB/s (2^40bytes or 10^9 bytes) (exact 2,000,000,000 bytes/sec)

# Did you know ?
- In 1us(time it takes light to travel 300m) py can do 68000 iters of an empty loop OR.
- py can do a max 100mill things in 1sec.

# References
- https://computers-are-fast.github.io/
- https://gist.github.com/hellerbarde/2843375
