"""
Problem
Print All Paths Of A Tree
Given a binary tree, return all paths from root to leaf.

Example One
{
"root": [1,
2, 3,
4, 5, 6, 7]
}
Output:
[
[1, 2, 4],
[1, 2, 5],
[1, 3, 6],
[1, 3, 7]
]
There are four leafs in the given graph, so we have four paths: from the root to every leaf. Each path is a list of the values from the tree nodes on the path, and we have four lists. They can go in any order.
"""

"""
For your reference:
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
"""
def all_paths_of_a_binary_tree(root):
    """
    Args:
     root(BinaryTreeNode_int32)
    Returns:
     list_list_int32
    """
    # Write your code here.
    """
    do dfs in preorder basis - NLR
    T:O(n) for traversing each node in the tree once
    S:n/2.n ~= O(n^2)
    """
    def dfs(root, sl, res):
        # base case
        if not root.left and not root.right:
            res.append(sl.copy())
            return
        # nested case
        if root.left:
            sl.append(root.left.value)
            dfs(root.left, sl, res)
            sl.pop()
        if root.right:
            sl.append(root.right.value)
            dfs(root.right, sl, res)
            sl.pop()
    # driver
    res = []
    if root is None: return []
    dfs(root, [root.value], res)    
    return res

