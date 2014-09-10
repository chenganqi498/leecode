# -*- coding: utf-8 -*-
# Implement regular expression matching with support for '.' and '*'.

# '.' Matches any single character.
# '*' Matches zero or more of the preceding element.

# The matching should cover the entire input string (not partial).

# The function prototype should be:
# bool isMatch(const char *s, const char *p)

# Some examples:
# isMatch("aa","a") → false
# isMatch("aa","aa") → true
# isMatch("aaa","aa") → false
# isMatch("aa", "a*") → true
# isMatch("aa", ".*") → true
# isMatch("ab", ".*") → true 
# isMatch("aab", "c*a*b") → true 

# This version exceeds time limit for large data set
class Solution:
    # @return a boolean
    def isMatch(self, s, p):
        ls, lp = len(s), len(p)  
        if lp == 0: return ls == 0
        
        if lp == 1 or p[1] != '*':
            if ls == 0 or p[0] != '.' and s[0] != p[0]:
                return False
            return self.isMatch(s[1:], p[1:])
        else:
            i = -1
            while i < ls and (i < 0 or p[0] == '.' or p[0] == s[i]):
                if self.isMatch(s[i+1:], p[2:]):
                    return True
                i += 1
            return False

if __name__ == '__main__':
    s, p = "aaaaaaaaaaaaab", "a*a*a*a*a*a*a*a*a*a*c"

    test = Solution()
    out = test.isMatch(s, p)