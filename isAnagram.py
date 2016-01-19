#Given two strings s and t, write a function to determine if t is an anagram of s.

#For example,
#s = "anagram", t = "nagaram", return true.
#s = "rat", t = "car", return false.

#Note:
#You may assume the string contains only lowercase alphabets.

class Solution:
    # @param {string} s
    # @param {string} t
    # @return {boolean}
    def isAnagram(self, s, t):
        if len(s) != len(t): return False
        s_dict, t_dict = {}, {}
        for i in range(len(s)):
            if s[i] not in s_dict:
                s_dict[s[i]] = 1
            else: s_dict[s[i]] += 1
            
            if t[i] not in t_dict:
                t_dict[t[i]] = 1
            else: t_dict[t[i]] += 1
        if s_dict == t_dict: return True
        else: return False