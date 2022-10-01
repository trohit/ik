"""
Problem
Segregate Even And Odd Numbers
Given an array of numbers, rearrange them in-place so that even numbers appear before odd ones.

Example
{
"numbers": [1, 2, 3, 4]
}
Output: [4, 2, 3, 1]
The order within the group of even numbers does not matter; same with odd numbers. So the following are also correct outputs: [4, 2, 1, 3], [2, 4, 1, 3], [2, 4, 3, 1].

Notes
It is important to practice solving this problem by rearranging numbers in-place.
There is no need to preserve the original order within the even and within the odd numbers.
We look for a solution of the linear time complexity that uses constant auxiliary space.

Constraints:
1 <= length of the array <= 105
1 <= element of the array <= 109
"""

def segregate_evens_and_odds(numbers):
    """
    Args:
     numbers(list_int32)
    Returns:
     list_int32
    """
    # Write your code here.
    even, odd = [], []
    for i, v in enumerate(numbers):
        if v % 2: # odd
            odd.append(v)
        else:
            even.append(v)
    return even + odd


# try - 2
def is_even(num):
    return False if num %2 else True
    
def segregate_evens_and_odds(numbers):
    """
    Args:
     numbers(list_int32)
    Returns:
     list_int32
    """
    # Write your code here.
    even, odd = [], []
    a = numbers
    n = len(a)
    l, r = 0, n - 1 
    while l<r:
        # print(f"{a} l:{l} r:{r} {a[l]}<>{a[r]}")
        if is_even(numbers[l]): l += 1
        if not is_even(numbers[r]): r -= 1
        if l < r and not is_even(a[l]) and is_even(a[r]):
            # print(f"{a} swap l:{l} r:{r} {a[l]}<>{a[r]}")
            a[l], a[r] = a[r], a[l] # swap l and r nums
    return a



# try - 3
def segregate_evens_and_odds(A):
    """
    Args:
     numbers(list_int32)
    Returns:
     list_int32
    """
    # Write your code here.
    n = len(A)
    j = 0
    # both i and j start at 0
    # i ptr moves right unconditionally
    # j slower ptr, only incremented when 
    #     i is even elm
    #     then i and j swap
    #     j incremented
    
    # looks for even elm
    # works faster due to cache coherence
    # 
    # and gets swapped
    n = len(A)
    j = 0
    for i in range(n):
        print(f"i:{i} j:{j} a:{A}")
        if A[i] % 2 == 0:
            # print(f"    {A[i]}<>{A[j]}")
            A[i], A[j] = A[j], A[i]
            j += 1
    return A
    
    return []

