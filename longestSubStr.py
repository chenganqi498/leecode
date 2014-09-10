# Given a string, 
# find the length of the longest substring without repeating characters. 
# For example, 
# the longest substring without repeating letters for "abcabcbb" is "abc", 
# which the length is 3. 
# For "bbbbb" the longest substring is "b", with the length of 1.

class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        if s == '': return 0
        i, l, maxi = 0, 0, 0
        record = {}
        while i < len(s):
           while i < len(s) and (s[i] not in record or record[s[i]] < i - l):
              record[s[i]] = i
              i += 1
              l += 1
           maxi = max(maxi, l) 
           if i < len(s): 
              l = i - record[s[i]] 
              record[s[i]] = i 
           i += 1
        return maxi

if __name__ == '__main__':
   s = "wlrbbmqbhcdarzowkkyhiddqscdxrjmowfrxsjybldbefsarcbynecdyggxxpklorellnmpapqfwkhopkmco"
   test = Solution()
   out = test.lengthOfLongestSubstring(s)
   print out
