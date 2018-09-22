#easy


# Write a method anagram(s,t) to decide if two strings are anagrams or not.

# Example
# Given s = "abcd", t = "dcab", return true.
# Given s = "ab", t = "ab", return true.
# Given s = "ab", t = "ac", return false.

# Challenge
# O(n) time, O(1) extra space

# Clarification
# What is Anagram?

# Two strings are anagram if they can be the same after change the order of characters.

class Solution:
    """
    @param s: The first string
    @param t: The second string
    @return: true or false
    """

    #My solution(Jiuzhang Solution)
    #Using hash table(dictionary) to compare the frequency of chars in two strs.
    def anagram(self, s, t):
        # write your code here
        cs = {}
        ct = {}
        if not s or not t:
            return False
        ls = len(s)
        lt = len(t)
        
        if ls != lt:
            return False
        
        i = 0
        while i < ls:
            if s[i] in cs:
                cs[s[i]] +=1
            else:
                cs[s[i]] =1
            if t[i] in ct:
                ct[t[i]] +=1
            else:
                ct[t[i]] =1
            i+=1
        return cs == ct

testcase = Solution()
print(testcase.anagram('paper','title'))