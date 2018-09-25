# medium

# Given a binary search tree (See Definition) and a node in it, find the in-order successor of that node in the BST.

# If the given node has no in-order successor in the tree, return null.

# Example
# Given tree = [2,1] and node = 1:

#   2
#  /
# 1
# return node 2.

# Given tree = [2,1,3] and node = 2:

#   2
#  / \
# 1   3
# return node 3.

# Challenge
# O(h), where h is the height of the BST.

# Notice
# It's guaranteed p is one node in the given tree. (You can directly compare the memory address to find p)

"""
Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""


class Solution:
    """
    @param: root: The root of the BST.
    @param: p: You need find the successor node of p.
    @return: Successor of p.
    """
#My solution (Jiuzhang solution)
#dfs likewise
    def inorderSuccessor(self, root, p):
        # write your code here
        if not root or not p:
            return None
        
        if root.val <= p.val:
            return self.inorderSuccessor(root.right,p)
        
        else:
            
            temp = self.inorderSuccessor(root.left,p)
            if  temp != None:
                return temp
            else:
                return root
