# Gven a string S and a string T, 
# find the minimum window in S which will contain all the characters in T in complexity O(n).

# For example,
# S = "ADOBECODEBANC"
# T = "ABC"
# Minimum window is "BANC".

# Note:
# If there is no such window in S that covers all characters in T, 
# return the emtpy string "".

# If there are multiple such windows, 
# you are guaranteed that there will always be only one unique minimum window in S.

class Solution:
    # @return a string
    def minWindow(self, S, T):
        if S == '' or T == '': return ''
        uniqT, window = {}, {}
        for i in range(len(T)):
            if T[i] not in uniqT: uniqT[T[i]] = 1
            else: uniqT[T[i]] += 1
        start, i, count = 0, 0, 0
        minLen = float('inf')
        minWin = ''

        while i < len(S):
            while i < len(S) and count < len(T):
                if S[i] in uniqT:
                   if S[i] not in window: window[S[i]] = 1
                   else: window[S[i]] += 1
                   if window[S[i]] <= uniqT[S[i]]: count += 1
                i += 1
            if count < len(T): break
            for j in range(start, i):
               if S[j] in uniqT:
                  window[S[j]] -= 1
                  if window[S[j]] < uniqT[S[j]]: 
                     count -= 1
                     break
            if i-j < minLen:
               minWin = S[j:i]
               minLen = i-j
            start = j+1

        return minWin

if __name__ == '__main__':
   S = "ADOBECODEBANC"
   T = "ABC" 
   test = Solution()
   out = test.minWindow(S, T)
   print out
