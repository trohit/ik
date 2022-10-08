"""
L295
Online Median
Given a list of numbers, the task is to insert these numbers into a stream and find the median of the stream after each insertion.
If the median is a non-integer, consider it’s floor value.
The median of a sorted array is defined as the middle element when the number of elements is odd and 
the mean of the middle two elements when the number of elements is even.

Example
{
"stream": [3, 8, 5, 2]
}
Output:[3, 5, 5, 4]
Iteration	Stream	Sorted Stream	Median
1	[3]	[3]	3
2	[3, 8]	[3, 8]	(3 + 8) / 2 => 5
3	[3, 8, 5]	[3, 5, 8]	5
4	[3, 8, 5, 2]	[2, 3, 5, 8]	(3 + 5) / 2 => 4
Notes
Constraints:
1 <= length of stream <= 105
1 <= any value in the stream <= 105
The stream can contain duplicates.
"""
"""
Approach
Brute Force: 
Sort arr in nlogn using Merge / Heap / Quick Sort. 
Use insertion sort to insert each elm into sorted arr. - O(n)
Do it n times 
Brute Force T:O(n^2) S: O(n)


Optimal Approach: 2 heaps small(max) and large(min)
always push new elm i to small 

if odd: pick middle elm n//2
if even: pick m-1 |m+1/2

01235
if 
odd: n//2
even: ((n//2)-1) + (n//2)/2
len  med
1    0
2    (0+1)/2
3    1
4    (1+2)/2
5    2

1. always push to small
2. if small[0] < large[0] then rebalance
3. if len(small) > len(large) + 1 or vice-versa: then rebalance by pop from one and push to other
4. get median
    4.1 case1 : odd
        4.1.1 if len(small) > len(large): med small[0]
        4.1.2 if len(large) > len (small): med = large[0]
    4.2 caes 2: even
        4.2.1 if len(small) == len(large): med = (s[0] + l[0])//2
n elms   
T: O(n*logn) where in worst case
  n is the total length
  3 pops + 2 pushes to heaps - O(5logn) 
  + peek O(1)
  
S: O(n)
"""
from heapq import heappush as hpush, heappop as hpop
def online_median(stream):
    # Write your code here.
    s, l, res = [], [], []
    med = 0
    # <maxheap>  > <minheap>
    for i in stream:
        print(f"add {i}")
        # maxq ... minq
        hpush(s, -1 * i)

        # maintain l>=s
        if s and l and -1*s[0] > l[0]:
            # print(f"  s>l", end=":")
            v = -1 * hpop(s)
            hpush(l, v)
        # print(f"  ph1: s:{s} l:{l}")
        
        # unequal len
        if len(s) > len(l) + 1:
            # print(f"  ls>>ll")
            v = -1 * hpop(s)
            hpush(l, v)
        elif len(s)+1  < len(l):
            # print(f"  ls<<ll")
            v = hpop(l)
            hpush(s, -1 * v)

        # print(f"  ph2: s:{s} l:{l}", end=":")
        # get median
        if len(s) > len(l): # if odd but s> l
            med = -1 * s[0]
        elif len(l) > len(s): # odd but l>s
            med = l[0]
        else: # even
            sv = -1 * s[0]
            lv = l[0]
            med = (sv + lv) // 2
        # print(f"med: {med}")
        res.append(med)
    return res
