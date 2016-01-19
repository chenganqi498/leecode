# Given a string s and a dictionary of words dict, 
<<<<<<< HEAD
# add spaces in s to construct a sentence where each word is a valid dictionary word.

# Return all such possible sentences.

# For example, given
# s = "catsanddog",
# dict = ["cat", "cats", "and", "sand", "dog"].

# A solution is ["cats and dog", "cat sand dog"].

# time limit exceed
class Solution2(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: List[str]
        """
        self.sent = []
        self.search(s, 0, wordDict, [])
        return self.sent

    def search(self, s, start, wordDict, cur):
        if start == len(s): return cur
        j = 1
        while j+start <= len(s):
            if s[start:start+j] in wordDict:
                if cur == []: new = [s[start:start+j]]
                else: new = [i+' '+s[start:start+j] for i in cur]
                self.search(s, start+j, wordDict, new)
            j += 1
        
        return 
              
class Solution2(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: List[str]
        """
        self.sent = []
        self.len = len(s)
        self.possible = [True]*len(s)
        self.search(s, wordDict, [])
        
        return self.sent

    def search(self, s, wordDict, cur):
        if len(s) == 0: 
            self.sent += cur
            return 0
        res = len(s)
        for j in range(1, len(s)): 
            if s[:j] in wordDict and self.possible[self.len-len(s)] == True:
                if cur == []: new = [s[:j]]
                else: new = [i+' '+s[:j] for i in cur]
                res = min(res, self.search(s[j:], wordDict, new))
            print s, j, res, self.possible
        if res > 0: self.possible[self.len-len(s)] = False    
        
        
=======
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


>>>>>>> c9daaa8fc778290aa4bd8c08de16455ca9112257
