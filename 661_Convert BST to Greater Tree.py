#easy


# Given a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to the original key plus sum of all keys greater than the original key in BST.

# Example
# Given a binary search Tree `{5,2,13}｀:

#               5
#             /   \
#            2     13
# Return the root of new tree

#              18
#             /   \
#           20     13


"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the root of binary tree
    @return: the new root
    """
    #My solution(Jiuzhang Solution)
    def dfs(self,node):
        if not node:
            return None
        dfs(self.node.right)
        sum+=node.val
        node.val = sum
        dfs(self.node.left)
    def convertBST(self, root):
        # write your code here
        dfs(root)
        return root