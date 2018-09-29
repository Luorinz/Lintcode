# hard

# 849. Basic Calculator III
# Implement a basic calculator to evaluate a simple expression string.

# The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, non-negative integers and empty spaces .

# The expression string contains only non-negative integers, +, -, *, / operators , open ( and closing parentheses ) and empty spaces . The integer division should truncate toward zero.

# You may assume that the given expression is always valid. All intermediate results will be in the range of [-2147483648, 2147483647]

# Example
# "1 + 1" = 2
# " 6-4 / 2 " = 4
# "2*(5+5*2)/3+(6/2+8)" = 21
# "(2+6* 3+5- (3*14/7+2)*5)+3"=-12
# Notice
# Do not use the eval built-in library function.

class Solution:
    """
    @param s: the expression string
    @return: the answer
    """
    def is_num(self,s):
        if s.isnumeric():
            return True
        elif s[0] == '-' and s[1:].isnumeric():
            return True
        else:
            return False

    def cal(self, s):
        # Calculate within the ()
        stack = []
        o1= ['+','-']
        #print(s)
        
        l = len(s)
        i = 0
        res = 0
        while i < l:
            #operate on the stack
            stack.append(s[i])
            i += 1
            #print("before check:",stack)
            # check the stack status
            try:
                while self.is_num(stack[-1])and (stack[-2] in o1) and self.is_num(stack[-3]) :
                    if stack[-2] == '+':
                        res = int(stack[-1]) + int(stack[-3])
                    elif stack[-2] == '-':
                        res = int(stack[-3]) - int(stack[-1])
                    stack.pop()
                    stack.pop()
                    stack.pop()
                    stack.append(str(res))
            except IndexError:
                pass    
            #print("after check:",stack)

        return str(stack.pop())

    def calculate(self, s):
        # Write your code here
        stack = []
        lp_stack = []

        o1= ['+','-']
        o2 = ['*','/']
        p = ['(',')']
        sign = o1 + o2 + p

        s = s.strip()
        l = len(s)
        i = 0
        res = 0

        while i < l:
            #operate on the stack
            if s[i] == ' ':
                i+=1
            if i<l and s[i] in sign:
                stack.append(s[i])
                if s[i] == '(':
                    lp_stack.append(len(stack) - 1)
                elif s[i] == ')':
                    
                    if lp_stack != []:
                        temp_stack = stack[lp_stack[-1]+1 : -1]
                        templ = len(temp_stack)
                        temp = self.cal(temp_stack)
                        for j in range(templ + 1):
                            stack.pop()
                        stack[lp_stack[-1]] = temp
                        lp_stack.pop()
                        
                i+=1
            curr_num = ""
            while i<l and self.is_num(s[i]) :
                curr_num += s[i]
                i+=1
            if curr_num:
                stack.append(curr_num)
            print("before check:",stack)

            #check the stack status
            try:
                while self.is_num(stack[-1]) and (stack[-2] in o2) and self.is_num(stack[-3]) :
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
                        if len(stack) >=1 and not self.is_num(stack[-1]):
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
        return int(stack.pop())


t = Solution()
print(t.calculate("(3-(5-(8)-(2+(9-(0-(8-(2))))-(4))-(4)))"))
