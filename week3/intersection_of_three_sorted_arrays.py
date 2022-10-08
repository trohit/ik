"""
L1213 https://leetcode.com/problems/intersection-of-three-sorted-arrays/
Problem: Intersection Of Three Sorted Arrays
Given three arrays sorted in the ascending order, return their intersection sorted array in the ascending order.

Example One
{
"arr1": [2, 5, 10],
"arr2": [2, 3, 4, 10],
"arr3": [2, 4, 10]
}
Output:[2, 10]

Example Two
{
"arr1": [1, 2, 3],
"arr2": [],
"arr3": [2, 2]
}
Output:[-1]

Example Three
{
"arr1": [1, 2, 2, 2, 9],
"arr2": [1, 1, 2, 2],
"arr3": [1, 1, 1, 2, 2, 2]
}
Output:

[1, 2, 2]
Notes
If the intersection is empty, return an array with one element -1.
Constraints:

0 <= length of each given array <= 105
0 <= any value in a given array <= 2 * 106

"""



"""
Approach: Brute Force Soln.
cmp 1st elm of each arr into res arr.
if all eq, then add to res arr else incr ptr with min val  
T: O(n)
S: O(n)
"""
def find_intersection(arr1, arr2, arr3):
    """
    Args:
     arr1(list_int32)
     arr2(list_int32)
     arr3(list_int32)
    Returns:
     list_int32
    """
    # Write your code here.
    a1,a2,a3 = arr1,arr2,arr3
    i,j,k = 0,0,0
    x,y,z = len(arr1), len(arr2), len(arr3)
    res = []
    while i<x and j<y and k<z:
        # print(f"i:{i} j:{j} k:{k} => {a1[i]} {a2[j]} {a3[k]}")
        if a1[i] == a2[j] and a2[j] == a3[k]: 
            # print(f"appending {a1[i]}")
            res.append(a1[i])
            i+=1;j+=1;k+=1
        else:
            if a1[i] <= a2[j] and a1[i] <= a3[k]:
                # print(">>i")
                i+=1
            elif a2[j] <= a1[i] and a2[j] <= a3[k]:
                # print(">>j")
                j+=1
            else:
                # print(">>k")
                k+=1
    if len(res) == 0: return [-1] 
    return res
