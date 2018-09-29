# medium

# 980. Basic Calculator II
# Implement a basic calculator to evaluate a simple expression string.

# The expression string contains only non-negative integers, +, -, *, / operators and empty spaces . The integer division should truncate toward zero.

# You may assume that the given expression is always valid.

# Example
# "3+2*2" = 7
# " 3/2 " = 1
# " 3+5 / 2 " = 5
# Notice
# Do not use the eval built-in library function.

class Solution:
    """
    @param s: the given expression
    @return: the result of expression
    """
    def calculate(self, s):
        # Write your code here


        stack = []
        o1= ['+','-']
        o2 = ['*','/']
        operator = o1+o2
        s = s.strip()
        
        print(s)
        
        l = len(s)
        i = 0
        res = 0
        while i < l:
            #operate on the stack
            
            if s[i] == " ":
                i+=1
            elif i<l and s[i] in operator:
                stack.append(s[i])
                i+=1
            else:
                curr_num = ""
                while i < l and s[i].isnumeric():
                    curr_num+=s[i]
                    i+=1
                if curr_num:
                    stack.append(curr_num)
            print("before check:",stack)

            # check the stack status
            try:
                while stack[-1].isnumeric and (stack[-2] in o2) and stack[-3].isnumeric() :
                    if stack[-2] == '*':
                        res = int(stack[-1]) * int(stack[-3])
                    elif stack[-2] == '/':
                        res = int(stack[-3]) // int(stack[-1])
                    if res != 0:
                        stack.pop()
                        stack.pop()
                        stack.pop()
                        stack.append(str(res))
                    else:
                        stack.pop()
                        stack.pop()
                        stack.pop()
                        if len(stack) >=1 and not stack[-1].isnumeric():
                            stack.pop()   
            except IndexError:
                pass    
            print("after check:",stack)
        ls = len(stack)
        k = 0
        while k < ls-1:
            if stack[k].isnumeric and (stack[k+1] in o1) and stack[k+2].isnumeric() :
                if stack[k+1] == '+':
                    res = int(stack[k]) + int(stack[k+2])
                elif stack[k+1] == '-' :
                    res = int(stack[k]) - int(stack[k+2])
                stack[k+2] = str(res)
            k+=2
            print(stack[k:])  
        return res

t = Solution()
print(t.calculate("100-1-2-3-4-5-6-7-8-9-10"))
        
        