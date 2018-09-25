# medium

# Given a binary tree, collect a tree's nodes as if you were doing this: Collect and remove all leaves, repeat until the tree is empty.

# Example
# Given binary tree:

#     1
#    / \
#   2   3
#  / \     
# 4   5    
# Returns [[4, 5, 3], [2], [1]].

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

# My solution
# divide and conquer
#use height to identify the layers
class Solution:
    """
    @param: root: the root of binary tree
    @return: collect and remove all leaves
    """
    def dfs(self,root,ans):
        if not root:
            return 0
        height = max(self.dfs(root.left,ans),self.dfs(root.right,ans)) + 1
        try:
            ans[height-1].append(root.val)
        except IndexError:
            ans.append([root.val])
        return height

    def findLeaves(self, root):
        # write your code here
        ans = []
        self.dfs(root,ans)
        return ans
