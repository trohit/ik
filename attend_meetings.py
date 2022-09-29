"""
Attend Meetings
Given a list of meeting intervals where each interval consists of a start and an end time, check if a person can attend all the given meetings such that only one meeting can be attended at a time.

Example One
{
"intervals": [[1, 5], [5, 8], [10, 15]]
}
Output:1
As the above intervals are non-overlapping intervals, it means a person can attend all these meetings.

Example Two
{
"intervals": [[1, 5], [4, 8]]
}
Output:0
Time 4 - 5 is overlapping in the first and second intervals.

Notes
A new meeting can start at the same time the previous one ended.

Constraints:
1 <= number of intervals <= 105
0 <= start time < end time <= 109
"""
def can_attend_all_meetings(intervals):
    """
    Args:
     intervals(list_list_int32)
    Returns:
     int32
    """
    # Write your code here.
    ii = intervals
    ii.sort()
    # print(ii)
    """
    a b
        c    d
    """
    a, b = [0, 0]
    for i in range(len(ii)):
        c, d = ii[i][0], ii[i][1]
        # print(f"a:{a} b:{b}")
        # print(f"c:{c} d:{d}")
        if b > c:
            return 0 # cannot attend
        a,b = c,d
    return 1 # can attend
