#Easy


# Given two strings s and t, determine if they are isomorphic.

# Two strings are isomorphic if the characters in s can be replaced to get t.

# All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

# Example
# Given s = "egg", t = "add", return true.

# Given s = "foo", t = "bar", return false.

# Given s = "paper", t = "title", return true.

# Notice
# You may assume both s and t have the same length.

class Solution:
    """
    @param s: a string
    @param t: a string
    @return: true if the characters in s can be replaced to get t or false
    """
    def isIsomorphic(self, s, t):
        # write your code here

        #My solution 
        #O(n) = n
        if not s or not t:
            return True
        length = len(s)
        dic1 = {}
        dic2 = {}
        for i in range(length):
            if s[i] not in dic1:
                dic1[s[i]] = t[i]
            elif dic1[s[i]] != t[i] :
                return False
        for i in range(length):
            if t[i] not in dic2:
                dic2[t[i]] = s[i]
            elif dic2[t[i]] != s[i] :
                return False
        return True

testcase = Solution()
print(testcase.isIsomorphic('paper','title'))
print(testcase.isIsomorphic("aab","bbc"))
print(testcase.isIsomorphic(
"a`%ii,VEZQc_BSU%ObO5<sX81B/bOw+CNUd#Uav*P!Ax!#>hh,k#b/|>4ixFQZl+l!?bJjakbQbGglEb<g>Hf81m@A9GIvbd]qh?y__t+E(Iyv7zUEfZF{81VaM-0u?]tG=_fFR/XJ=X{-,oRpxE9u*VNYlM",
"b`%ii-WE[Qc_BSV%OcO5<sX82B/cOw+CNVd#Vbv*P!Bx!#?hh-k#c/|?4ixFQ[l+l!?cJkbkcQcGhlEc<h?Hf82m@B9GIvcd]rh?y__t+E(Iyv7{VEf[F{82WbN/0u?]tG=_fFR/XJ=X{/-oRpxE9u*WNYlN"
))



