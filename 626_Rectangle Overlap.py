#Easy

# Given two rectangles, find if the given two rectangles overlap or not.

# Example
# Given l1 = [0, 8], r1 = [8, 0], l2 = [6, 6], r2 = [10, 0], return true

# Given l1 = [0, 8], r1 = [8, 0], l2 = [9, 6], r2 = [10, 0], return ``false`

# Notice
# l1: Top Left coordinate of first rectangle.
# r1: Bottom Right coordinate of first rectangle.
# l2: Top Left coordinate of second rectangle.
# r2: Bottom Right coordinate of second rectangle.

# l1 != r2 and l2 != r2

"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""

class Solution:
    """
    @param l1: top-left coordinate of first rectangle
    @param r1: bottom-right coordinate of first rectangle
    @param l2: top-left coordinate of second rectangle
    @param r2: bottom-right coordinate of second rectangle
    @return: true if they are overlap or false
    """
    def doOverlap(self, l1, r1, l2, r2):
        # write your code here

        #My solution
        #Discuss the situation when not overlapped
        
        if r1.y>l2.y or l1.y < r2.y:
            #up and down
            return False
        elif r1.x < l2.x or l1.x >r2.x:
            #left and right
            return False
        else:
            return True
