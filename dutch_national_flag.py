"""
Problem
Dutch National Flag
Given some balls of three colors arranged in a line, rearrange them such that all the red balls go first, then green and then blue ones.

Do rearrange the balls in place. A solution that simply counts colors and overwrites the array is not the one we are looking for.
This is an important problem in search algorithms theory proposed by Dutch computer scientist Edsger Dijkstra. Dutch national flag has three colors (albeit different from ones used in this problem).

Example
{
"balls": ["G", "B", "G", "G", "R", "B", "R", "G"]
}
Output:

["R", "R", "G", "G", "G", "G", "B", "B"]
There are a total of 2 red, 4 green and 2 blue balls. In this order they appear in the correct output.

Notes
Constraints:
1 <= n <= 100000
Do this in ONE pass over the array, NOT TWO passes
Solution is only allowed to use constant extra memory
"""
"""
0..i: <mid
i..j: ==mid
j..k: unsorted
k..n: >mid

0 .....i... j.......... k ...n
 <mid   mid   unsorted   >mid

1. initially i and j start at the same place from the left, k starts from r..l.
2. loop j from 0..n-1
3. whenever elm<mid is seen: swap(a[j], a[i]); i++,j++
4. whenever elm>mid is seen: swap(a[j], a[k]); k--
5. else elm == mid: j++ 

procedure three-way-partition(A : array of values, mid : value):
    i ← 0
    j ← 0
    k ← size of A - 1
    while j <= k:
        if A[j] < mid:
            swap A[i] and A[j]
            i ← i + 1
            j ← j + 1
        else if A[j] > mid:
            swap A[j] and A[k]
            k ← k - 1
        else:
            j ← j + 1
"""
def dutch_flag_sort(balls):
    """
    Args:
     balls(list_char)
    Returns:
     list_char
    """
    # uses 3 way partition sort
    # https://en.wikipedia.org/wiki/Dutch_national_flag_problem
    a = balls
    # Write your code here.
    n = len(a)
    i,j,k = 0,0,n-1
    # RGB
    mid = "G"
    while j<=k:
        # disp(a,i,j,k)
        
        if a[j] == 'R':#< mid:
            a[i], a[j] = a[j], a[i]
            i+=1
            j+=1
        elif a[j] == 'B': #> mid:
            a[j], a[k] = a[k], a[j]
            k-=1
        else: # a[j] == mid aka G
            j+=1
    # T:O(n)
    return a

# Alternate faster implemention

def dutch_flag_sort(balls):
    """
    Args:
     balls(list_char)
    Returns:
     list_char
    """
    # Write your code here.
    n= len(balls)
    bptr =n-1
    # loop for bptr
    for i in range(n-1,-1,-1):
         #print(f"i {i} balls{balls[i]}")
         if balls[i] == 'B':
             balls[bptr], balls[i] = balls[i], balls[bptr]
             bptr -= 1
    
    rptr = 0
    for i in range(0, bptr+1):
        if balls[i] == 'R':
            balls[rptr], balls[i] = balls[i], balls[rptr]
            rptr += 1
    return balls
          
    
