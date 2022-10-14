"""
Problem
Fibonacci Number
Given a number n, find the n-th Fibonacci Number.

Example
{
"n": 2
}
Output:1
2nd Fibonacci Number is the sum of the 0th and 1st Fibonacci Number = 0 + 1 = 1.
"""

def find_fibonacci(n):
    """
    Args:
     n(int32)
    Returns:
     int32
    """
    # Write your code here.
    
    def helper(n, a, b ):
        if n == 0:
            return a
        else:
            return helper(n-1, b, a + b)
    return helper(n, 0, 1)

  # mine
  dd = {0:0,1:1}
def find_fibonacci(n):
    """
    Args:
     n(int32)
    Returns:
     int32
    """
    # Write your code here.
    # 1 1 2 3 5 8
    # base case
    if n == 0 or n == 1: return dd[n]
    if n-1 in dd:
        x= dd[n-1]
    else:
        x= find_fibonacci(n -1)
        dd[n-1] = x
    if n-2 in dd:
        y= dd[n-2]
    else:
        y= find_fibonacci(n -2)
        dd[n-2]= y
    return x+y
