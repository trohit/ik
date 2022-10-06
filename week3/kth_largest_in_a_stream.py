"""
Kth Largest In A Stream
Given an initial list along with another list of numbers to be appended with the initial list and an integer k,
return an array consisting of the k-th largest element after adding each element from the first list to the second list.

Example
{
"k": 2,
"initial_stream": [4, 6],
"append_stream": [5, 2, 20]
}
Output:
[5, 5, 6]
"""
import heapq
def kth_largest(k, initial_stream, append_stream):
    """
    Args:
     k(int32)
     initial_stream(list_int32)
     append_stream(list_int32)
    Returns:
     list_int32
    """
    # Write your code here.
    a1 = initial_stream
    len_stream = len(a1)
    res = [] # output buffer
    heapq.heapify(a1) # (A) O(a) 
    cur_min = 0
    # assume len(a1)=a and len(a2)=b
    while len(a1) > k: # a - k times
        tmp = heapq.heappop(a1) # (B) (a-k)*log(a-k)
        # print(f"popping {tmp}")
        
    # print(f"ini: {a1}")
    for j in append_stream: # b times
        heapq.heappush(a1, j) # (C) b*log(a+b)
        while len(a1) > k:
            cur_min = heapq.heappop(a1) # (D) b*log(a+b)
        kth = a1[0]
        # print(f"inloop: {a1} cur_min:{cur_min} {kth}")
        res.append(kth)
    return res
    # T: O(b*log(a+b))
    # S: k
