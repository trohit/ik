# Tables


## How many bytes make a ..?
2^..
20 Mill megs : 10^6
30 Bill gigs : 10^9
40 Trillion tubs : 10^12
50 Quadrillion (1000 trill) pubs : 10^15

```
Number unit.       Mem unit.     Sci notation   Binary / logn base2
Thousand (K).      KB.                 10^3                      2^10
Million (M).           MB.                10^6                        2^20
Billion (B).             GB.                 10^9                       2^30
Trillion (T).            TB.                  10^12                    2^40
Quadrillion.           PB.                  10^15                   2^50  (1000 trillion)
```


## Time Complexity
- 1 < logn  < n  <  nlogn  < n2  < 2^n <  n! < n^n
- hash  binsrch  linear heapsort bubble fib     
```
O(1) = constant
O(log n) = logarithmic
O(n) = linear
O(n log n) = linearithmic
O(n^2) = quadratic
O(n^3) = cubic
O(2^n) = exponential
```

## Power of a modern PC
- a modern cpu can do about 100 mill basic math ops / sec => 10^2.10^6 = 10^8 ops /sec, each op takes ~10ns
- a supercomputer is about 10000 times faster than a single cpu => 10^12 ops/sec 

# How many ns in a sec
1 sec = 10^3ms = 10^9 ns (a bill. ns)

# how many bits to represent ..
- Num # of bits needed to represent 'n' states =  [log2(n) + 1]
  -  1 bit to store 2 states
  -  2 bits to store 4 states
  -  4 bits to store 16 states
  -  8 bits to store 256 states
  - 15 bits to store 32768 states
  - 16 bits to store 65536 states
  - 30 bits to store 1 bill states
  - 32 bits to store 4 bill states
 
