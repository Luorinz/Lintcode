# easy

# For a given source string and a target string, you should output the first index(from 0) of target string in source string.

# If target does not exist in source, just return -1.

# Have you met this question in a real interview?  
# Clarification
# Do I need to implement KMP Algorithm in a real interview?

# Not necessary. When you meet this problem in a real interview, the interviewer may just want to test your basic implementation ability. But make sure you confirm with the interviewer first.
# Example
# If source = "source" and target = "target", return -1.

# If source = "abcdabcdefg" and target = "bcd", return 1.

# Challenge
# O(n2) is acceptable. Can you implement an O(n) algorithm? (hint: KMP)


# Built-in function solution
class Solution:
    """
    @param source: 
    @param target: 
    @return: return the index
    """
    def strStr(self, source, target):
        # Write your code here
        return source.find(target)