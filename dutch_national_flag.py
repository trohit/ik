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
    return a
