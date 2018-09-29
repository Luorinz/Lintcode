# hard

# 978. Basic Calculator
# Implement a basic calculator to evaluate a simple expression string.

# The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, non-negative integers and empty spaces .

# You may assume that the given expression is always valid.

# Example
# "1 + 1" = 2
# " 2-1 + 2 " = 3
# "(1+(4+5+2)-3)+(6+8)" = 23
# Notice
# Do not use the eval built-in library function.

#My solution
#Use stack to simulate
class Solution:
    """
    @param s: the given expression
    @return: the result of expression
    """
    def calculate(self, s):
        # Write your code here
        def is_num(s):
            if s.isnumeric():
                return True
            elif s[0] == '-' and s[1:].isnumeric():
                return True
            else:
                return False
        stack = []
        operator = ['+','-']
        
        parentheses = ['(',')']
        sign = operator+parentheses
        s = s.strip()
        l = len(s)
        i = 0
        res = 0
        while i < l:
            #operate on the stack
            if s[i] == ' ':
                if i <l:
                    i+=1
            if i<l and s[i] in sign:
                stack.append(s[i])
                i+=1
            

            curr_num = ""
            while i<l and is_num(s[i]) :
                curr_num += s[i]
                if i < l:
                    i+=1
                
            if curr_num:
                stack.append(curr_num)
            #print("before check:",stack)

            #check the stack status
            flag = True
            try:
                while flag:
                    flag = False
                    while is_num(stack[-1]) and (stack[-2] in operator) and (is_num(stack[-3]) ):
                        if stack[-2] == '+':
                            res = int(stack[-1]) + int(stack[-3])
                        elif stack[-2] == '-':
                            res = int(stack[-3]) - int(stack[-1])
                        stack.pop()
                        stack.pop()
                        stack.pop()
                        stack.append(str(res))
                        flag = True
                    while stack[-1] == ")" and stack[-3] == "(" and is_num(stack[-2]):
                        stack.pop()
                        stack.pop(-2)
                        flag = True
            except IndexError:
                pass
           # print("after check:",stack)

  
            
        return res

t = Solution()
print(t.calculate("(1+(4+5+2)-3)+(6+8)"))



            
           

