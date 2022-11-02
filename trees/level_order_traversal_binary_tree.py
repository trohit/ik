"""
Level Order Traversal Of A Binary Tree
Given a binary tree, list the node values level by level from left to right.

Notes
Constraints:
1 <= number of nodes in the given tree <= 20000
0 <= node value < number of nodes
Node values are unique

Example 1:
{
"root": [0,
1, null,
null, 2,
4, null,
null, 3]
}

Out:
[[0],[1],[2],[4],[3]]

"""

"""
For your reference:
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
"""
def level_order_traversal(root):
    """
    Args:
     root(BinaryTreeNode_int32)
    Returns:
     list_list_int32
    """
    # Write your code here.
    # T:O(n)
    # S:O(n)
    ## base case 
    # q = {node1, node2...} sa we use BFS
    # out = {n1.val, n2.val,...}
    if not root: return
    q, out = [root], []
    while q: # while q has elms
        tout, cnt = [], len(q) # tout stores all nodes in this lvl 
        while cnt: # cnt stores cnt of all nodes in a lvl
            # print(f"cnt:{cnt}")
            tn = q.pop(0)
            if tn.left:
                # print(f"appending l:{tn.left.value}")
                q.append(tn.left)
            if tn.right:
                # print(f"appending r:{tn.right.value}")
                q.append(tn.right)
            tout.append(tn.value)
            cnt -= 1
        # print(f"appending nodes in this lvl:{tout}")
        out.append(tout)
    return out
