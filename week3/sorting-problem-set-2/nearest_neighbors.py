"""
Problem:Nearest Neighbors
Given coordinates of a point p and n other points on a two-dimensional surface, find k points out of n which are the nearest to point p.
Distance is measured by the standard Euclidean method.

Example One
{
"p_x": 1,
"p_y": 1,
"k": 1,
"n_points": [
[0, 0],
[1, 0]
]
}
Output:
[
[1, 0]
]
The distance of point {0, 0} from point p{1, 1} is sqrt(2) and that of point {1, 0} is 1. We need to choose 1(k) point having the minimum distance from point p. So it is {1, 0}.

Example Two
{
"p_x": 1,
"p_y": 1,
"k": 2,
"n_points": [
[1, 0],
[2, 1],
[0, 1]
]
}
Output:
[
[1, 0],
[2, 1]
]
We can see that there are all the points are at the same distance from point p. So the answer can be any 2 points. Here {{1, 0}, {0, 1}} and {{2, 1}, {0, 1}} are all equally acceptable answers.

Notes
Constraints:
1 <= n <= 100000
k <= n
-1000000000 <= coordinates of points <=1000000000
"""

"""

A. BruteForce: compute n distances, then sort n elms(heap/merge/quick), then display first k elms. T: O(nlogn) S:O(n+k)
B. Sub-optimal: keep max heap of 3 elms. for each dist computed, if dist_list < k, push into heap else push n pop. T: O(n.logk) S:O(n+k) 
C. Optimal: compute all dists. Then use qsel to successively partition randomly until k-1th elm is found. T:O(n)...O(n^2)  S:O(n+k) 

Time Complexity: O(n.logk)
Space Complexity: O(k)
"""
import heapq
def nearest_neighbours(p_x, p_y, k, n_points):
    """
    Args:
     p_x(int32)
     p_y(int32)
     k(int32)
     n_points(list_list_int32)
    Returns:
     list_list_int32
    """
    # Write your code here.
    min_dists = []
    
    for q in n_points:
        d = math.sqrt((p_x - q[0]) ** 2 + (p_y - q[1]) ** 2)
        if len(min_dists) < k:
            heapq.heappush(min_dists, (-d, q))
        else:
            heapq.heappushpop(min_dists, (-d, q))
    print(min_dists)
    return [q for (d, q) in min_dists]
