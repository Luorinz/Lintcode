# easy

# 627. Longest Palindrome
# Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.

# This is case sensitive, for example "Aa" is not considered a palindrome here.

# Example
# Given s = "abccccdd" return 7

# One longest palindrome that can be built is "dccaccd", whose length is 7.

# Notice
# Assume the length of given string will not exceed 1010.


class Solution:
    """
    @param s: a string which consists of lowercase or uppercase letters
    @return: the length of the longest palindromes that can be built
    """
    def longestPalindrome(self, s):
        # write your code here
        #Init
        if not s:
            return 0
        l = len(s)
        if l == 1:
            return 1
        dic = {}
        for i in s :
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1

        count = 0
        count_1 = 0
        for v in dic.values():
            if v % 2 == 0:
                count += v
            elif v%2 != 0 and v!=1:
                count += (v -1)
                count_1 += 1
            else:
                count_1+=1
        if count_1 != 0:
            count+=1
        return count

t = Solution()
print(t.longestPalindrome("abccccdd"))