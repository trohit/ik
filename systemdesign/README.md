# Tables


## How many bytes make a ..?
2^..
20 Mill megs : 10^6
30 Bill gigs : 10^9
40 Trillion tubs : 10^12
50 Quadrillion (1000 trill) pubs : 10^15

## alternate mnemonic to remember pow(2)
millionaire by 20
billionaire by 30
trillionaire by 40
quadrillionaire by 50

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

```
def gets_bits_to_store_states(states):
    return ceil( log2(states) )
```
![image](https://user-images.githubusercontent.com/466385/200450017-c506abd2-f619-4eb0-b286-1d9d7126231f.png)


# Uptime
## Availability Table - Cheat sheet
What you need to remember

| Availability level    | Downtime per year |
|-----------------------|-------------------|
| 90% ("one nine")      | 36.5 days         |
| 95%                   | 18.25 days        |
| 99% ("two-nines")     | 3.65 days         |
| 99.50%                | 1.83 days         |
| 99.9%("three nines")  | 8.76 hours        |
| 99.95%                | 4.38 hours        |
| 99.99%("four nines")  | 52.6 minutes      |
| 99.999%("five nines") | 5.26 minutes      |

- https://gist.githubusercontent.com/dastergon/07751e9d3117ae0ead808cd39d4f92d1/raw/4515c0db813d45abf0ba2770123c26c311393ef7/availability-cheatsheet.md

| Availability level    | Downtime per year | Downtime per quarter | Downtime per month | Downtime per week | Downtime per day | Downtime per hour |
|-----------------------|-------------------|----------------------|--------------------|-------------------|------------------|-------------------|
| 90% ("one nine")      | 36.5 days         | 9 days               | 3 days             | 16.8 hours        | 2.4 hours        | 6 minutes         |
| 95%                   | 18.25 days        | 4.5 days             | 1.5 days           | 8.4 hours         | 1.2 hours        | 3 minutes         |
| 99% ("two-nines")     | 3.65 days         | 21.6 hours           | 7.2 hours          | 1.68 hours        | 14.4 minutes     | 36 seconds        |
| 99.50%                | 1.83 days         | 10.8 hours           | 3.6 hours          | 50.4 minutes      | 7.20 minutes     | 18 seconds        |
| 99.9%("three nines")  | 8.76 hours        | 2.16 hours           | 43.2 minutes       | 10.1 minutes      | 1.44 minutes     | 3.6 seconds       |
| 99.95%                | 4.38 hours        | 1.08 hours           | 21.6 minutes       | 5.04 minutes      | 43.2 seconds     | 1.8 seconds       |
| 99.99%("four nines")  | 52.6 minutes      | 12.96 minutes        | 4.32 minutes       | 60.5 seconds      | 8.64 seconds     | 0.36 seconds      |
| 99.999%("five nines") | 5.26 minutes      | 1.30 minutes         | 25.9 seconds       | 6.05 seconds      | 0.87 seconds     | 0.04 seconds      |
