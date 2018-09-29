# easy

# 604. Window Sum
# Given an array of n integer, and a moving window(size k), move the window at each iteration from the start of the array, find the sum of the element inside the window at each moving.

# Example
# For array [1,2,7,8,5], moving window size k = 3.
# 1 + 2 + 7 = 10
# 2 + 7 + 8 = 17
# 7 + 8 + 5 = 20
# return [10,17,20]

class Solution:
    """
    @param nums: a list of integers.
    @param k: length of window.
    @return: the sum of the element inside the window at each moving.
    """
    def winSum(self, nums, k):
        # write your code here
        if not nums:
            return []
        l = len(nums)
        if l<k:
            return []
            
            
        ans = []
        ans.append(sum(nums[:k]))
        i = k
        while i < l:
            temp = ans[i-k] - nums[i-k] + nums[i]
            ans.append(temp)
            i+=1
        return ans
                
            