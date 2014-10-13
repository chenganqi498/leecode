# Implement wildcard pattern matching with support for '?' and '*'.

# '?' Matches any single character.
# '*' Matches any sequence of characters (including the empty sequence).

# The matching should cover the entire input string (not partial).

# The function prototype should be:
# bool isMatch(const char *s, const char *p)

# Some examples:
# isMatch("aa","a") -> false
# isMatch("aa","aa") -> true
# isMatch("aaa","aa") -> false
# isMatch("aa", "*") -> true
# isMatch("aa", "a*") -> true
# isMatch("ab", "?*") -> true
# isMatch("aab", "c*a*b") -> false

# dp[i][j] = s[:i] matches p[:j]
class Solution:
    # @param s, an input string
    # @param p, a pattern string
    # @return a boolean
    def isMatch(self, s, p):
        ls, lp = len(s), len(p)
        dp = [[False]*(lp+1) for i in range(ls+1)]
        dp[0][0] = True
        i, j = 0, 0
        while i < ls and j < lp:
              if dp[i][j] == True and \
                     p[j] == s[i] or p[j] == '?':
                 dp[i+1][j+1] = True
                 i += 1
                 j += 1    
              elif p[j] == '*':  
                 for k in range(i,ls): dp[k+1][j+1] = True
                 j += 1
              else: return False
        if i == ls: return p[j:] == '*'*(lp-j)
        return dp[ls][lp] 
                
if __name__ == '__main__':
   test = Solution()
   out = test.isMatch('hi','*?')
   print out
