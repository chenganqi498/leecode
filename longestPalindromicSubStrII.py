# Given a string S, find the longest palindromic substring in S. 
# You may assume that the maximum length of S is 1000, 
# and there exists one unique longest palindromic substring.

# DP solution, still exceed time limit on large data set
class Solution:
    # @return a string
    def longestPalindrome(self, s):
        l = len(s)
        if l == 0 or l == 1: return s
        maxlen = 1
        index = [0,0]

        P = [[0]*l for i in range(l)]
        for j in range(l):
            for i in range(j+1):
                if i == j: P[i][j] = True
                elif i+1 == j: P[i][j] = s[i] == s[j]
                else: P[i][j] = s[i] == s[j] and P[i+1][j-1] 
 
               if P[i][j] == True and j-i+1 > maxlen:
                   maxlen = j-i+1
                   index = [i,j]
                       
        return s[index[0]:index[1]+1]
 
if __name__ == '__main__':
   s = 'aaaaa'
   test = Solution()
   out = test.longestPalindrome(s)
   print out

