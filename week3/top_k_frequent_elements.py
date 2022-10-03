"""
L347 Top K Frequent Elements

Top K Frequent Elements
Given an integer array and a number k, find the k most frequent elements in the array.

Example One
{
"arr": [1, 2, 3, 2, 4, 3, 1],
"k": 2
}
Output: [3, 1]

Example Two
{
"arr": [1, 2, 1, 2, 3, 1],
"k": 1
}
Output: [1]
Notes
If multiple answers exist, return any.
The order of numbers in the output array does not matter.

Constraints:
1 <= length of the given array <= 3 * 105
0 <= array element <= 3 * 105
1 <= k <= number of unique elements in the array

Soln:
https://www.youtube.com/watch?v=YPTqKIgVk-k
"""

def find_top_k_frequent_elements(arr, k):
    """
    Args:
     arr(list_int32)
     k(int32)
    Returns:
     list_int32
    """
    """
    n   c
    1   2
    2   2
    3   2
    4   1
    
    0     1    2      
    [[], [4], [1,2,3]] 
    """
    # Write your code here.
    a = arr
    n = len(a)
    cnt = {}
    # counting sort - O(n) ->(A)
    for i, v in enumerate(a):
        cnt[v] = cnt.get(v, 0) + 1
    # print(f"cnt:{cnt}")
    # invert such that freqlist[0..n] O(n) -> (B)
    freq_ll = [[] for i in range( (n+1)) ]
    # print(f"freq:{freq_ll}")
    
    for n, c in cnt.items():
        freq_ll[c].append(n)
    # print(f"freq:{freq_ll}")
    
    # compact the freq_ll to only store non 0 freq
    res = []
    for i in range(len(freq_ll)-1, 0, -1):
        for n in freq_ll[i]:
            res.append(n)
            if len(res) == k:
                # print(f"res:{res}")
                return res
    return freq_ll[k]



# alternate heap sort approach
import heapq
def find_top_k_frequent_elements(arr, k):
    """
    Args:
     arr(list_int32)
     k(int32)
    Returns:
     list_int32
    """
    # Write your code here.
    
    if len(arr) <= 1 or k == len(arr): 
        return arr
        
    hashmap = {}
    
    for i in arr:
        if i in hashmap:
            hashmap[i] = hashmap[i] + 1
        else:
            hashmap[i] = 1
    
    return heapq.nlargest(k, hashmap.keys(), hashmap.get)
