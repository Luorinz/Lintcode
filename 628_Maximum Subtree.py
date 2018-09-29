# easy

# 628. Maximum Subtree
# Given a binary tree, find the subtree with maximum sum. Return the root of the subtree.

# Example
# Given a binary tree:

#      1
#    /   \
#  -5     2
#  / \   /  \
# 0   3 -4  -5 
# return the node with value 3.

# Notice
# LintCode will print the subtree which root is your return node.
# It's guaranteed that there is only one subtree with maximum sum and the given binary tree is not an empty tree.
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
    @return: the maximum weight node
    """
    def __init__(self):
        self.result = None
    def dfs(self,root,sum,stack):
        if not root :
          return 0
        temp = sum
        temp += self.dfs(root.left,sum,stack)
        temp += self.dfs(root.right,sum,stack)
        temp += root.val
        sum = temp
        
        if not stack:
            stack.append(sum)
            self.result = root
        else:
            if sum > stack[0]:
                stack[0] = sum
                self.result = root
        
        return sum
        
    def findSubtree(self, root):
        # write your code here
        if not root :
          return None
        sum = 0
        stack = []
        self.dfs(root,sum,stack)
        return self.result
        