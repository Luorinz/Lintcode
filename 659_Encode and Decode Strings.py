#Medium

# Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.

# Please implement encode and decode

# Example
# Given strs = ["lint","code","love","you"]
# string encoded_string = encode(strs)

# return ["lint","code","love","you"] when you call decode(encoded_string)


# My solution(Jiuzhang Solution)
# Use : to transfer concatenation operator
# O(n) =n
# beat 69.9%
class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        # write your code here
        res = ""
        for i in range(len(strs)):
            for k in range(len(strs[i])):
             
                if strs[i][k] == ":":
                    res +="::"
                else:
                    res+=strs[i][k]
            res+=":;"

        return res

    """
    @param: str: A string
    @return: dcodes a single string to a list of strings
    """
    def decode(self, str):
        # write your code here
        res = []
        curr = ""
        l = len(str)
        i = 0
        while i < l:
            if str[i] == ":":
                if str[i+1] == ":":
                    i+=2
                    curr+=":"
                elif str[i+1] == ";":
                    i+=2
                    res.append(curr)
                    curr = ""
            else:
                curr+=str[i]
                i+=1
        return res

#Jiuzhang Solution

    def encode1(self, strs):
        # write your code here
        for str in strs:
            for word in str:
                if word == ":":
                    word = "::"
        res = ":;".join(strs) + ":;"
        return res

    
    """
    @param: str: A string
    @return: dcodes a single string to a list of strings
    """
    def decode1(self, str):
        # write your code here
        
        res = []
        i = 0
        j = 0
       
        while i < len(str):
            i += 1
            if i < len(str) and  str[i] == ":" and str[i -1 ] == ":":
                i += 1
                
            if i < len(str) and str[i] == ";" and str[i - 1 ] == ":":
                res.append( str[j:i-1])
                j = i+1
                i += 1 
                
        return res


testcase = Solution()
a = testcase.encode(["lint","code","love","you"])
print(a)
print(testcase.decode(a))