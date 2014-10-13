# Given a string s and a dictionary of words dict, 
# determine if s can be segmented into a space-separated sequence of one or more dictionary words.

# For example, given
# s = "leetcode",
# dict = ["leet", "code"].

# Return true because "leetcode" can be segmented as "leet code".

# p[start][end] is whether s[start:end] can be segmented
class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a boolean
    def wordBreak(self, s, dict):
        ls = len(s)
        p = [[False]*(ls+1) for i in range(ls)]
        for end in range(1, ls+1):
            for start in range(end-1, -1, -1):
                if s[start:end] in dict: p[start][end] = True
                else:
                    for mid in range(start+1, end): 
                        temp = p[start][mid] and p[mid][end]
                        if temp == True: 
                           p[start][end] = True
                           break
        return p[0][ls]

if __name__ == '__main__':
   s = 'pplovelppp'
   dict = ['pp','love','lp']
   test = Solution()
   out = test.wordBreak(s, dict)
   print out


