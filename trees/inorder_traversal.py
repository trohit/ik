
"""
For your reference:
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
"""
def inorder(root):
    """
    Args:
     root(BinaryTreeNode_int32)
    Returns:
     list_int32
    """
    # Write your code here.
    res = []
    def bst_inorder_r(root):# LNR
        nonlocal res
        if not root: return
        if root.left:bst_inorder_r(root.left)
        res.append(root.value)
        if root.right:bst_inorder_r(root.right)

    # https://www.techiedelight.com/inorder-tree-traversal-iterative-recursive/
    def bst_inorder_i(root):# LNR in stack: RNL
        res, st = [], []
        node = root
        while st or node:
            if node:
                st.append(node)
                node = node.left
            else:
                node = st.pop()
                res.append(node.value)
                node = node.right
        return res
        
    res = bst_inorder_i(root)    
    # bst_inorder_r(root)
    return res
