"""
Generate Binary Strings Of Length N
Given a number n, generate all possible binary strings of length n.
Example
{
"n": 3
}
Output:
["000", "001", "010", "011", "100", "101", "110", "111"]

Notes
A string consisting of only 0s and 1s is called a binary string.
Return the output list in any order.

Constraints:
1 <= n <= 16
"""

# T:O(n.2^n)
# S:O(n.2^n)
def get_binary_strings(n):
    """
    Args:
     n(int32)
    Returns:
     list_str
    """
    # Write your code here.
    def bt(sl, res, n):
        if len(sl) == n:
            res.append("".join(sl))
            return
        sl.append('0')
        bt(sl, res, n)
        sl.pop()
        sl.append('1')
        bt(sl, res, n)
        sl.pop()
    res = []
    bt([], res, n)        
    return res

  
# Optimal approach 2
def get_binary_strings(n):
    result = list()
    helper('', n, result)
    return result

def helper(num, n, result):
    # base case
    if n == 1:
        result.append(num + '0')
        result.append(num + '1')
        return

    # Recursive case
    helper(num + '0', n-1, result)
    helper(num + '1', n-1, result)
    return

# Optimal approach 3
lists = []
def helper(current_string, n):
    if n == 0:
        ## return the whole string as no more characters to add; partial solution is now the full solution
        lists.append(current_string)
        return
    else:
        ## increase the partial solution with one character
        ## decrease the subproblem by 1 (i.e. n); don't need to pass in anything else for the next subproblem as can only add 0 and 1
        helper(current_string + "0", n-1)
        helper(current_string + "1", n-1)

def get_binary_strings(n):
    helper("", n)
    return lists
    
