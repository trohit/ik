"""
Problem
Merge One Sorted Array Into Another
First array has n positive numbers, and they are sorted in the non-descending order.
Second array has 2n numbers: first n are also positive and sorted in the same way but the last n are all zeroes.
Merge the first array into the second and return the latter. You should get 2n positive integers sorted in the non-descending order.

Example
{
"first": [1, 3, 5],
"second": [2, 4, 6, 0, 0, 0]
}
Output: [1, 2, 3, 4, 5, 6]

Notes
Constraints:
1 <= n <= 105
1 <= array elements (except those zeroes) <= 2 * 109
You can use only constant auxiliary space
"""
def merge_one_into_another(first, second):
    """
    Args:
     first(list_int32)
     second(list_int32)
    Returns:
     list_int32
    """
    # Write your code here.
    """
    merge first and second such that elms from 
    second are inserted into first
    """
    i,j,k = len(first)-1, len(first)-1, len(second)-1 
    while i>=0 and j>=0:
        if first[i] >= second[j]:
            second[k] = first[i]
            i-=1
        else:
            second[k] = second[j]
            j-=1
        k-=1
    while i>=0:
        second[k] = first[i]
        i-=1
        k-=1
    while j>=0:
        second[k] = second[j]
        j-=1
        k-=1
    return second
