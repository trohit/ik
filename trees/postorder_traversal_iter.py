"""
PostOrder Traversal Without Recursion
Given a binary tree, find its post-order traversal without using recursion.

Input:
{
"root": [100,
200, 300,
400, 500]
}

Output:
[400, 500, 200, 300, 100]
"""

"""
For your reference:
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
"""
def disp(st):
    print("[", end="")
    for i in st:
        print(f"{i.value}", end=",")
    print("]", end="")
        
# https://www.techiedelight.com/postorder-tree-traversal-iterative-recursive/       
def postorder_traversal(root):
    """
    Args:
     root(BinaryTreeNode_int32)
    Returns:
     list_int32
    """
    # Write your code here.
    res, st = [], [root]
    while st:
        node = st[-1] # peek into stack
        #print(f"n:{node.value}", end="=>"); disp(st); print(f"res:{res}")
        if node.left:
            st.append(node.left)
            node.left = None
        elif node.right:
            st.append(node.right)
            node.right = None
        else:
            st.pop()
            res.append(node.value)
    return res

