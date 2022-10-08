
"""
Objective
1. to determine any int not thats not present in arr.
 
Constraints:
1 <= length of input array <= 200000
0 <= element of input array < 2^32

observation
1. each of the 4 bill ints can be between 0..(4x2^30)
2. dup elms can be present.
3. we can use a hashmap if we had enough mem but we do not. Only have 10MB mem.
4. Nothing in the problem says we cant use the same mem as a crude hashmap.
5. no -ve nums will be seen in the arr. so any -ve num can be used to denote special significance.

strategy:
1. store each elm at its correct index.
2. if squat_elm seen at its index, then
    2.1 while num not at corr. loc.
        2.1.1 swap(squat_elm <> elm@squat_index)
        2.1.2 if num at index out of bounds, discard and store -1
3. loop and search for 1st index having -1, thats the missing elm

T:O(n)
S:O(1)

Related:
https://stackoverflow.com/questions/7153659/generate-an-integer-that-is-not-among-four-billion-given-ones
https://leetcode.com/problems/missing-number/solution/
"""
def find_integer(arr):
    """
    Args:
     arr(list_int64)
    Returns:
     int64
    """
    # Write your code here.
    a = arr
    n = len(a)
    for i in range(n):
        # print(f"a:{a} checking if {i} exists in corr pos")
        while a[i] != i and a[i] != -1:
            squat_elm = a[i]
            if squat_elm >= n: 
                # print(f"{squat_elm} too big, discarding")
                a[i] = -1
            else:
                # print(f"swap {i}<>{a[i]} -> {a[i]}, {a[squat_elm]}")
                a[i], a[squat_elm] = a[squat_elm], a[i]
                # print(f"postswap:{a}")
    for i in range(n):
        if a[i] == -1:
            # print(f"found missing elm {i}")
            return i    
    # print(f"no missing elm, so ret {n}")
    return n

