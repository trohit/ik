"""

Problem: Sort All Characters
Given a list of characters, sort it in the non-decreasing order based on ASCII values of characters.

Example
{
"arr": ["a", "s", "d", "f", "g", "*", "&", "!", "z", "y"]
}
Output:["!", "&", "*", "a", "d", "f", "g", "s", "y", "z"]
Notes
Constraints:
1 <= length of the list <= 100000
Input list consists of alphanumeric characters and these ones: !, @, #, $, %, ^, &, *, (, ).
"""
"""
Approach:
just use a hashmap to implement counting sort as teh num of uniq elms are a small const as compared to arr len n . 
1. sort : n log n
2. counting sort : O(n) +O(n)
"""
def sort_array(arr):
    """
    Args:
     arr(list_char)
    Returns:
     list_char
    """
    # Write your code here.
    hmap = {}
    for i in (arr):
        if i in hmap:
            hmap[i] += 1
        else:
            hmap[i] = 1
    i = 0
    keys = list(hmap.keys())
    keys.sort()
    # print(f"keys:{keys}")
    # print(f"hmap:{hmap}")
    for ch in keys:
        for t in range(hmap[ch]):
            arr[i] = ch
            i+=1
    # print(arr)
    return arr
