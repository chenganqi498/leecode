# Write a function to find the longest common prefix string 
# among an array of strings.

class Solution:
    # @return a string
    def longestCommonPrefix(self, strs):
        if strs == []: return ''
        prefix = strs[0]
        for s in strs[1:]:
            new = ''
            for j in range(min(len(prefix), len(s))):
                if prefix[j] == s[j]:
                   new += s[j]
                else: break
            prefix = new
            if prefix == '': return ''
        return prefix

if __name__ == '__main__':
   strs = ['pp','p']
   test = Solution()
   out = test.longestCommonPrefix(strs)
   print out
