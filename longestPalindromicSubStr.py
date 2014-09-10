# Given a string S, find the longest palindromic substring in S. 
# You may assume that the maximum length of S is 1000, 
# and there exists one unique longest palindromic substring.

# this version exceeds time limit on large data set
class Solution:
    # @return a string
    def longestPalindrome(self, s):
        l = len(s)
        if l == 0: return s
        sub = s[0]
        s1, e1, s2, e2 = 0, 1, 0 ,1
        for i in range(1, l):
           if i > 0 and s[i] == s[i-1]:
              [s1, e1] = self.palindrome(s, i-1, i)
              sub = s[s1:e1] if e1-s1 > len(sub) else sub
           if s1 > 0 and i > 1 and s[i] == s[i-2]: 
              [s2, e2] = self.palindrome(s, i-2, i)
              sub = s[s2:e2] if e2-s2 > len(sub) else sub             
           if len(sub) == l: return s
        return sub              

    def palindrome(self, s, start, end):
        while end < len(s)-1 and start > 0 and s[end+1] == s[start-1]:
              end += 1
              start -= 1
        return [start, end+1]

if __name__ == '__main__':
   s = 'abcdeed'
   test = Solution()
   out = test.longestPalindrome(s)
   print out

