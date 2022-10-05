"""
Problem : Kth Largest In An Array
Given an array of integers, find the k-th largest number in it.

Example One
{
"numbers": [5, 1, 10, 3, 2],
"k": 2
}
Output:5

Example Two
{
"numbers": [4, 1, 2, 2, 3],
"k": 4
}
Output:2

Notes
Constraints:
1 <= array size <= 3 * 105
-109 <= array elements <= 109
1 <= k <= array size

Approach:
keep qsel until pivot elem == n -k
each qsel :O(n)
T: in worst case: O(n^2)
T: in practice : O (n log n)
S: O(1) as no extra space used
actually k log n
so if k much smaller than n
then better than nlogn sorting algos
"""
def qsel(a, k, l, r):
    # using lomuto partitioning
    # lets use a random int as pivot elm => piv
    rand_index = random.randint(l, r)
    a[rand_index], a[r] = a[r], a[rand_index]
    p, piv = l, a[r]
    # print(f"a:{a} k:{k} p:{p} piv:{piv} l:{l} r:{r} {a[l:r]}")
    
    for i in range(l, r):
        # print(f"  {a}  cmp i:{i} p:{p} {a[i]} <= {piv}")
        if a[i] <= piv:
            # print(f"    swap {p}<>{i} {a[p]}<>{a[i]}")
            a[i], a[p] = a[p], a[i]
            p += 1
    # swap piv <> a[p]
    a[p], a[r] = a[r], a[p]
    # print(f"postpart: a:{a} k:{k} piv:{piv} p:{p} l:{l} r:{r} {a[l:r]}")
    if p > k: # k p
        return qsel(a, k, l, p - 1)
    elif p < k:# p k
        return qsel(a, k, p + 1, r)
    else: # p == k
        return piv
    
def kth_largest_in_an_array(numbers, k):
    """
    Args:
     numbers(list_int32)
     k(int32)
    Returns:
     int32
    """
    # Write your code here.
    a = numbers
    n = len(a)
    if n == 1: return a[0]
    k = n - k # actual offset of k in partitioned array
    res = qsel(a, k, 0, n - 1)
    return res
