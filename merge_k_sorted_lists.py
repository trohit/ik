"""
Merge K Sorted Linked Lists
Given k linked lists where each one is sorted in the ascending order, merge all of them into a single sorted linked list.

Example
{
  "lists": [
    [1, 3, 5],
    [3, 4],
    [7]
  ]
}

Output:[1, 3, 3, 4, 5, 7]

Notes
Constraints:
0 <= k <= 104
0 <= length of any given linked list <= 103
-109 <= node values <= 109
Sum of the lengths of all given lists won't exceed 105.

"""
For your reference:
class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next = None
"""
import heapq
def merge_k_lists(lists):
    """
    Args:
     lists(list_LinkedListNode_int32)
    Returns:
     LinkedListNode_int32
    """
    # Write your code here.
    ll = lists
    hl = []
    rl = LinkedListNode(-1)
    tl = rl
    # stash all nodes to the heap : O(k*n) = O(N) where - (A)
    #   k is the num of lists
    #   n is the num of elms in each list
    #   N = k*n
    for l in ll:
        tp = l
        while tp:
            hl.append(tp.value)
            tp = tp.next
    # now heapify this heap list: O(logN)              - (B)
    heapq.heapify(hl)
    while hl:# N times so O(NlogN)                     - (C)
        v = heapq.heappop(hl) # O(logN)
        # print(f"min elm seen at lindex {minli} with v: {lptrs[minli].value}")#=>{ll[minli]}")
        tl.next = LinkedListNode(v)
        tl = tl.next
    return rl.next
    # O(N) + O(logN) + O(NlogN) ~ O(NlogN) 
