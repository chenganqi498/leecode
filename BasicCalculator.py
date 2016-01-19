#Implement a basic calculator to evaluate a simple expression string.

#The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, non-negative integers and empty spaces .

#You may assume that the given expression is always valid.

#Some examples:

#"1 + 1" = 2
#" 2-1 + 2 " = 3
#"(1+(4+5+2)-3)+(6+8)" = 23

#Note: Do not use the eval built-in library function. 

class Solution:
    # @param {string} s
    # @return {integer}
    def calculate(self, s):
        self.stack = []
        i = 0
        while i < len(s):
            if s[i] == ' ':
                i += 1
            elif s[i] in ['+', '_', '(']:
                self.stack.append(s[i])
                i += 1
            elif s[i].isdigit():
                j = i+1
                while j < len(s) and s[j].isdigit():
                    j += 1
                self.operation(self.stack, s[i:j])
                i = j
            else:
                string = self.stack.pop()
                self.operation(self.stack, string)
                i += 1
        return self.stack[0]
            
    def operation(self, stack, string):
        if self.stack == []: 
            self.stack.append(int(string))
            return
        elif self.stack[-1] == '(':
            self.stack.pop()
            self.stack.append(int(string))
            return
        val = int(string)
        sign = self.stack.pop()
        if sign == '+':
            new_val = int(self.stack.pop())+val
        else:
            new_val = int(self.stack.pop())-val
        self.stack.append(new_val)   