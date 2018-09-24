class Solution:
    """
    @param digits: A digital string
    @return: all posible letter combinations
    """
    def dfs(x,l,string,digits,phone,ans):
        if x==1:
            ans.append(string)
            return 
        d = digits[x] - '0'
        for i in phone[d]):
            dfs(x + 1, l, string+ i, digits,phone,ans)
            
        
    def letterCombinations(self, digits):
        # write your code here
        
        phone = {"","","abc",
            "def","ghi","jkl","mno","pqrs","tuv","wxyz",
        }
        ans = []
        if not digits:
            return ans
        dfs(0,len(digits),"",digits,phone,ans)
        return ans

solution 2
 dfs not containing other args



