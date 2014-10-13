# Given a string containing just the characters '(' and ')', 
# find the length of the longest valid (well-formed) parentheses substring.

# For "(()", the longest valid parentheses substring is "()", which has length = 2.
# Another example is ")()())", where the longest valid parentheses substring is "()()", which has length = 4.

class Solution:
    # @param s, a string
    # @return an integer
    def longestValidParentheses(self, s):
        maxnum = 0
        tomatch = []
        for i in range(len(s)):
            if s[i] == '(': tomatch.append(i)
            else:
               if tomatch != [] and s[tomatch[-1]] == '(':
                  tomatch.pop()
                  temp = tomatch[-1] if tomatch != [] else -1 
                  maxnum = max(maxnum, i-temp)
               else: tomatch.append(i)
        return maxnum

if __name__ == '__main__':
   s = ")()())" 
   test = Solution()
   out = test.longestValidParentheses(s)
   print out


