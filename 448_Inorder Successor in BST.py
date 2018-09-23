#Medium

# Given a binary tree, determine if it is a valid binary search tree (BST).

# Assume a BST is defined as follows:

# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.
# A single node tree is a BST
# Example
# An example:

#   2
#  / \
# 1   4
#    / \
#   3   5
# The above binary tree is serialized as {2,1,4,#,#,3,5} (in level order).


"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: The root of binary tree.
    @return: True if the binary tree is BST, or false
    """
    def __init__(self):
    
   

    def isValidBST(self, root):
        # write your code here
        if not root:
            return True
        
        if not self.isValidBST(root.right.val): 
            return False
        else:
            if root.right.val <= root.val:
                return False
            else:
                return True
        if not self.isValidBST(root.left.val) :
            return False
        else:
            if root.left.val >= root.val:
                return False
            else: 
                return True

            