# hard

# Given a set of words without duplicates, find all word squares you can build from them.

# A sequence of words forms a valid word square if the kth row and column read the exact same string, where 0 ≤ k < max(numRows, numColumns).

# For example, the word sequence ["ball","area","lead","lady"] forms a word square because each word reads the same both horizontally and vertically.

# b a l l
# a r e a
# l e a d
# l a d y
# Example
# Given a set ["area","lead","wall","lady","ball"]
# return [["wall","area","lead","lady"],["ball","area","lead","lady"]]
# Explanation:
# The output consists of two word squares. The order of output does not matter (just the order of words in each word square matters).

# Given a set ["abat","baba","atan","atal"]
# return [["baba","abat","baba","atan"],["baba","abat","baba","atal"]]
# Explanation:
# The output consists of two word squares. The order of output does not matter (just the order of words in each word square matters).
# Notice
# There are at least 1 and at most 1000 words.
# All words will have the exact same length.
# Word length is at least 1 and at most 5.
# Each word contains only lowercase English alphabet a-z.


class Solution:
    """
    @param: words: a set of words without duplicates
    @return: all word squares
    """
    def dfs(self,cur_layer,words):
        max_layer = len(words[0])
        for i in range(max_layer):
            if cur_layer == 1:

    def wordSquares(self, item, words):
        # write your code here
        if not words:
            return []
        



testcase = Solution()
print(testcase.wordSquares(["area","lead","wall","lady","ball"]))


