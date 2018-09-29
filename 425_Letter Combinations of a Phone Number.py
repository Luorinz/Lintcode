# medium

# Given a digit string excluded 01, return all possible letter combinations that the number could represent.

# A mapping of digit to letters (just like on the telephone buttons) is given below.

# Cellphone

# Example
# Given "23"

# Return ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]

# Notice
# Although the above answer is in lexicographical order, your answer could be in any order you want.




#My solution
#do some modifications from Jiuzhang version
class Solution:
    """
    @param digits: A digital string
    @return: all posible letter combinations
    """
    # def dfs(self,d,s,num,dic,ans):
    #     if d==1:
    #         ans.append(s)
    #         return 
    #     d = int(num[d]) 
    #     for i in dic[d]):
    #         self.dfs(x + 1, string+ i, num,dic,ans)

    def dfs(self,d,s,num,dic,ans):
            l = len(num)

            if d == l :
                ans.append(s)
                return 
            currNum = int(num[d])
            for i in dic[currNum]:
                temp = s+i
                self.dfs(d+1,temp,num,dic,ans)
            
        
    def letterCombinations(self, num):
        # write your code here
        dic = ["","","abc",
            "def","ghi","jkl","mno","pqrs","tuv","wxyz",
        ]
        ans = []
        if not num:
            return ans
        s = ""
        d = 0
        self.dfs(d,s,num,dic,ans)
        return ans

testcase = Solution()
print(testcase.letterCombinations("23"))



