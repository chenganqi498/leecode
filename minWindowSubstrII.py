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

#this version ignore duplicates in T
class Solution:
    # @return a string
    def minWindow(self, S, T):
        if S == '' or T == '': return ''
        uniqT = {}
        for i in range(len(T)): uniqT[T[i]] = i
        start = 0
        minLen = float('inf')
        minWin = ''

        while start < len(S):
            i = start
            window = {}
            res = len(uniqT)
            while i < len(S) and res != 0:
                if S[i] in uniqT and S[i] not in window: res -= 1
                window[S[i]] = i
                i += 1
            if res != 0: break
            for j in range(start, i):
               if S[j] in uniqT and window[S[j]] == j: break
            if i-j < minLen:
               minWin = S[j:i]
               minLen = i-j
            start = j+1
            
        return minWin

if __name__ == '__main__':
   S = "a"
   T = "aa"
   print 'original', S
   test = Solution()
   out = test.minWindow(S, T)
   print out
