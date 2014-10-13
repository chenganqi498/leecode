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

# time limit exceed
class Solution:
    # @param s, an input string
    # @param p, a pattern string
    # @return a boolean
    def isMatch(self, s, p):
        if s == '' and p == '': return True
        i, j = 0, 0
        if i < len(s) and s[i] == '*': 
           for k in range(j, len(p)+1):
               if self.isMatch(s[i+1:], p[k:]) == True: return T
               return False
        elif j < len(p) and p[j] == '*':
           for k in range(i, len(s)+1):
               if self.isMatch(s[k:], p[j+1:]) == True: return True
           return False
        elif i < len(s) and j < len(p) and (s[i] == p[j] or s[i] == '?' or p[j] == '?'):
           return self.isMatch(s[i+1:], p[j+1:])
        else: return False

if __name__ == '__main__':
   test = Solution()
   out = test.isMatch("babaaababaabababbbbbbaabaabbabababbaababbaaabbbaaab", "***bba**a*bbba**aab**b")
   print out
