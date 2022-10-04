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
# T:O(klogn)
# S:O(n) hash + O(k) heap = O(n+k) 
import heapq
def find_top_k_frequent_elements(arr, k):
    n = len(arr)
    if n <= 1 or n == k: return arr # base case, if k == n all elms are uniq and equal freq
    hmap = {}
    for i in arr: # O(n) to create a hashmap 
        hmap[i] = hmap.get(i, 0) + 1
    print(f"hmap:{hmap}")
    top_k_elms = heapq.nlargest(k, hmap.keys(), hmap.get) # O(klogn) : k elms * extracted from heap logn
    print(f"top_{k}_elms:{top_k_elms}")
    return top_k_elms


# alternate counter counting sort approach
"""
T: O(k) + O((n - k) log k) + O(k log k) algorithm = approx O(n log k) , 
S: O(n) for counter + O(n) heap 
which is very good for a small constant k, since it's essentialy linear. 
The O(k) part comes from heapifying the initial k counts, 
the second part from n - k calls to heappushpop method and 
the third part from sorting the final heap of k elements.
https://stackoverflow.com/questions/29240807/python-collections-counter-most-common-complexity
"""
from collections import Counter
def find_top_k_frequent_elements(arr, k):
    n = len(arr)
    ctr = Counter(arr)
    top_k_elms = [elm for elm,count in ctr.most_common(k)]
    return top_k_elms
    
