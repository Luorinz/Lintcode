# medium

# Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

# Example
# Given [100, 4, 200, 1, 3, 2],
# The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.

# Clarification
# Your algorithm should run in O(n) complexity.

class Solution:
    """
    @param num: A list of integers
    @return: An integer
    """
    #my solution
    def longestConsecutive(self, num):
        # write your code here
        dic = {}
        ans = 0
        curr = 0
        for i in num:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i]+=1
        for i in num:
            curr = 0
            temp1 = i
            temp2 = i
            while temp1+1 in dic:
                dic.pop(temp1+1)
                temp1+=1
                curr+=1
            while temp2-1 in dic:
                dic.pop(temp2-1)
                temp2-=1
                curr+=1
            if curr > ans:
                ans = curr
            dic.pop(i,0)
        ans+=1
        return ans
        
testcase = Solution()
print(testcase.longestConsecutive([100, 4, 200, 1, 3, 2]))