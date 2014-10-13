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

# Finally got it !
class Solution:
    # @param s, an input string
    # @param p, a pattern string
    # @return a boolean
    def isMatch(self, s, p):
        ls, lp = len(s), len(p)
        i, j = 0, 0
        star = []
        while i < ls:
            if j<lp and (p[j] == s[i] or p[j] == '?'): 
               i, j = i+1, j+1
            elif j<lp and p[j] == '*':
               star = [i, j]
               j += 1
            elif star != []: 
               star[0] += 1
               i, j = star[0], star[1]+1 
            else: return False

        if i == ls and j == lp: return True
        elif i == ls: return p[j:] == '*'*(lp-j)
        else: return False

if __name__ == '__main__':
   test = Solution()
   out = test.isMatch('hi','*?')
   print out
