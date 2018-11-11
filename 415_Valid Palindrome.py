# medium

# Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

# Example
# "A man, a plan, a canal: Panama" is a palindrome.

# "race a car" is not a palindrome.

# Challenge
# O(n) time without extra memory.

# Notice
# Have you consider that the string might be empty? This is a good question to ask during an interview.

# For the purpose of this problem, we define empty string as valid palindrome.

class Solution:
    """
    @param s: A string
    @return: Whether the string is a valid palindrome
    """
    def isPalindrome(self, s):
        # write your code here
        # Use double pointers to solve this
        # Check input
        if s is None:
            return False
        if s.strip() == "":
            return True
        
        # Pre process the string
        s = s.strip()
        new_str = ""
        for i in s:
            if i.isalnum() is True:
                new_str += i.lower()
        
        # Double pointers
        left = 0
        right = len(new_str) - 1
        count = 0
        while left < right:
            if new_str[left] != new_str[right]:
                return False
            left += 1
            right -= 1
        return True