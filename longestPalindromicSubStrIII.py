# Given a string S, find the longest palindromic substring in S. 
# You may assume that the maximum length of S is 1000, 
# and there exists one unique longest palindromic substring.

class Solution:
    # @return a string
    def longestPalindrome(self, s):
        if len(s) <= 1: return s
       
        T = '#'
        for i in s: T += i+'#'
        
        longestCenter, center, right = 0, 0, 0
        maxlen = 1
        l = len(T)
        longestP = T[0]
        P = [0]*l
        for i in range(l):
           i_mirror = 2*center - i
           P[i] = 0 if i > right else min(P[i_mirror], right-i)
           while i-1-P[i] > -1 and i+1+P[i] < l \
                 and T[i+1+P[i]] == T[i-1-P[i]]:
                 P[i] += 1
           if P[i] + i > right: center, right = i, i + P[i]
           if P[i] > maxlen:
              maxlen = P[i] 
              longestCenter = i   
        return s[(longestCenter-maxlen)/2: (longestCenter+maxlen)/2]


if __name__ == '__main__':
   s = 'aaaaaaaaa'
   test = Solution()
   out = test.longestPalindrome(s)
   print s
   print out

