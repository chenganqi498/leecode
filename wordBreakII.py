# Given a string s and a dictionary of words dict, 
# add spaces in s to construct a sentence where each word is a valid dictionary word.

# Return all such possible sentences.

# For example, given
# s = "catsanddog",
# dict = ["cat", "cats", "and", "sand", "dog"].
# A solution is ["cats and dog", "cat sand dog"].

# p[start][end] is all possible ways that s[start:end] can be segmented
class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a boolean
    def wordBreak(self, s, dict):
        ls = len(s)
        p = [[] for i in range(ls+1)]
        for end in range(1,ls+1):
            if s[:end] in dict: p[end].append(s[:end])
            for mid in range(end, 0, -1):
                if s[mid:end] in dict:
                   for i in p[mid]: p[end].append(i+' '+ s[mid:end])
        return p[-1]

if __name__ == '__main__':
   s = 'pplovelp'
   dict = ['p','pp','love','lp']
   test = Solution()
   out = test.wordBreak(s, dict)
   print out


