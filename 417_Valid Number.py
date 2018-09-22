#hard

# Validate if a given string is numeric.

# Example
# "0" => true

# " 0.1 " => true

# "abc" => false

# "1 a" => false

# "2e10" => true

class Solution:
    """
    @param s: the string that represents a number
    @return: whether the string is a valid number
    """

    #My solution(Jiuzhang solution)
    #beat 100%
    #Be aware of the Null input and the index problem
    #num = space +/- floater e +/- int space

    def isNumber(self, s):
        # write your code here
        if not s :
            return False
        s = s.strip()
        l = len(s)
        i = 0
        
        if not s :
            return False        
            
        if s[i] == '+' or s[i] =='-':
            i+=1

        
        countd = 0
        countn = 0
        while i <l and (s[i] == '.' or s[i].isnumeric()) :
            if s[i] =='.':
                countd +=1
            if s[i].isnumeric():
                countn +=1
            i+=1


        if countd>1 or countn<=0:
            return False   
        
        if i ==l:
            return True
       
        if s[i] == 'e':
            i+=1
            if s[i] == '+' or s[i] =='-':
                i+=1
            if i ==l:
                return False
            while i < l:
                if not s[i].isnumeric():
                    return False
                i+=1
       
        return i == l
testcase = Solution()
print(testcase.isNumber("2ef10"))