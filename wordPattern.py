# Given a pattern and a string str, find if str follows the same pattern.

# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

# Examples:

#    pattern = "abba", str = "dog cat cat dog" should return true.
#    pattern = "abba", str = "dog cat cat fish" should return false.
#    pattern = "aaaa", str = "dog cat cat dog" should return false.
#    pattern = "abba", str = "dog dog dog dog" should return false.

# Notes:
# You may assume pattern contains only lowercase letters, and str contains lowercase letters separated by a single space. 

class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        s = s.split(' ')
        if len(s) != len(pattern):
           return False
        
        patndict = {}
        strdict = {}
        for i in range(len(pattern)):
            if pattern[i] not in patndict and s[i] not in strdict:
                patndict[pattern[i]] = s[i]
                strdict[s[i]] = pattern[i]
            elif pattern[i] in patndict and s[i] in strdict:
                if pattern[i] != strdict[s[i]]:
                 return False
            else: return False
        return True
        

            
                    
                
        