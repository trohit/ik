"""
Given a binary tree, return node values in the preorder traversal order.

"""

"""
For your reference:
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
"""
def preorder(root):
    """
    Args:
     root(BinaryTreeNode_int32)
    Returns:
     list_int32
    """
    # Write your code here.
    res = [] 
    st = [root] if root else []
    def pre_bst_r(root):
        nonlocal res
        if not root: return
        res.append(root.value)
        pre_bst_r(root.left)
        pre_bst_r(root.right)
        
    def disp(st):
        for i in st:
            print(f"{i.value}", end=",")
        print()
            
    def pre_bst(root):# NLR in stack RLN
        res, st = [], [root] if root else []
        while st:
            # print(f"st:{st}")
            # disp(st)
            node = st.pop()
            if node.right:
                st.append(node.right)
            if node.left:
                st.append(node.left)
            res.append(node.value)
        return res
        
    #pre_bst_r(root)
    res = pre_bst(root)
    return res
