# You are given a string, S, and a list of words, L, that are all of the same length. 
# Find all starting indices of substring(s) in S that is a concatenation of each word in L 
# exactly once and without any intervening characters.

# For example, given:
# S: "barfoothefoobarman"
# L: ["foo", "bar"]
# You should return the indices: [0,9].
# (order does not matter).

# exceed time limit
class Solution:
    # @param S, a string
    # @param L, a list of string
    # @return a list of integer
    def findSubstring(self, S, L):
        if L == [] or len(S) < len(L[0])*len(L): return []
        hashmap = {}
        for i in L:
            if i not in hashmap: hashmap[i] = 1
            else: hashmap[i] += 1
        unit = len(L[0])
        index = []
        for begin in range(unit):
            i = begin
            while i < len(S):
                match = {}
                start = i
                found = 0
                while i+unit-1<len(S) and S[i:i+unit] in hashmap:
                   if S[i:i+unit] not in match:
                      match[S[i:i+unit]] = [i]
                   else:
                      match[S[i:i+unit]].append(i)
                   if len(match[S[i:i+unit]]) == hashmap[S[i:i+unit]]:
                      found += 1   
                   elif len(match[S[i:i+unit]]) > hashmap[S[i:i+unit]]:
                      newstart = match[S[i:i+unit]][0]+unit
                      for j in range(start, newstart, unit):
                          if len(match[S[j:j+unit]]) == hashmap[S[j:j+unit]]:
                             found -= 1 
                          match[S[j:j+unit]].pop(0)
                      start = newstart
                   if found == len(hashmap): 
                      index.append(start)
                      match[S[start:start+unit]].pop(0)
                      found -= 1
                      start += unit 
                   i += unit
                i += unit
        return sorted(index)

if __name__ == '__main__':
   S = "barfoothefoobarman"
   L = ["foo", "bar"]

   test = Solution()
   out = test.findSubstring('abababab',['a','b','a'])
   print out
