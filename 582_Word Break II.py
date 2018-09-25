# hard


# Given a string s and a dictionary of words dict, add spaces in s to construct a sentence where each word is a valid dictionary word.

# Return all such possible sentences.

# Example
# Gieve s = lintcode,
# dict = ["de", "ding", "co", "code", "lint"].

# A solution is ["lint code", "lint co de"].

class Solution:
    """
    @param: s: A string
    @param: wordDict: A set of words.
    @return: All possible sentences.
    """
    def dfs(self,s, wordDict,memo):
        if s in memo:
            return memo[s] 
        ans = []
        for i in range(len(s)):
            s1 = s[:i+1]
            s2 = s[i+1:]
            if s1 in wordDict:
                s2_res = self.dfs(s2,wordDict,memo)
                for i in s2_res:
                    if not i:
                        ans.append(s1)
                    else:
                        ans.append(s1 + " " + i)
        memo[s] = ans

        return ans 



    def wordBreak(self, s, wordDict):
        # write your code here
        memo = {}
        memo[""] = []
        memo[""].append("")

        return self.dfs(s,wordDict,memo)
         

 
testcase = Solution()
# print(testcase.wordBreak("lintcode",["lint","code"]))
print(testcase.wordBreak("lintcode",["de", "ding", "co", "code", "lint"]))