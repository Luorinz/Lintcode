#medium


# Description
# A message containing letters from A-Z is being encoded to numbers using the following mapping:

# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
# Given an encoded message containing digits, determine the total number of ways to decode it.

# Example
# Given encoded message 12, it could be decoded as AB (1 2) or L (12).
# The number of ways decoding 12 is 2.



class Solution:
    """
    @param s: a string,  encoded message
    @return: an integer, the number of ways decoding
    """
    #My Solution
    #Use the same way as climbing stair problem
    #O(n) = n
    #beats 97%

    def numDecodings(self, s):
        # write your code here
        if not s or s=='0':
            return 0
        length = len(s)
        if length == 1:
            return 1
        prev = 1
        prev_prev = 1
        curr = 0
        for i in range(1,length):
            if  s[i]=='0':
                if s[i-1] == '0' or int(s[i-1] + s[i])>26:
                    return 0
                else:
                    curr=prev_prev
            elif int(s[i-1] + s[i]) <= 26 and int(s[i-1] + s[i]) > 10:
                curr=prev_prev +prev
            elif s[i-1]==0 and s[i] ==0:
                return 0
            else:
                curr = prev
            prev_prev = prev
            prev = curr
            
        return curr

    #best solution
    #use a list to store the results of nth digit.
    def numDecodings_best_solution(self, s):
        # Write your code here
        if s == "" or s[0] == '0':
            return 0

        dp=[1,1]
        for i in range(2,len(s) + 1):
            if 10 <= int(s[i - 2 : i]) <=26 and s[i - 1] != '0':
                dp.append(dp[i - 1] + dp[i - 2])
            elif int(s[i-2 : i]) == 10 or int(s[i - 2 : i]) == 20:
                dp.append(dp[i - 2])
            elif s[i-1] != '0':
                dp.append(dp[i-1])
            else:
                return 0

        return dp[len(s)]

testcase = Solution()
print(testcase.numDecodings('7452310519'))
print(testcase.numDecodings_best_solution('7452310519'))

