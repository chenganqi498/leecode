# Given a string S and a string T, count the number of distinct subsequences of T in S.

# A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not).

# Here is an example:
# S = "rabbbit", T = "rabbit"
# Return 3.

# wtf of the following ??? why are u expecting 3 ???
# Input:	"ccc", "c"
# Output:	1
# Expected:	3

class Solution:
    # @return an integer
    def numDistinct(self, S, T):
        if T == '': return 0
        i, cover, num = 0, 0, 0
        subseq = []
        for i in range(len(S)):
            j, count = 0, 0
            while j < len(T):
                if i+count< len(S) and S[i+count] == T[j]:
                   count += 1
                j += 1
            if i+count > cover: 
               cover = i+count
               if S[i:i+count] not in subseq:
                  subseq.append(S[i:i+count])
                  num += 1
        return num

if __name__ == '__main__':
   S = "rabbbit"
   T = "rabbit"
   test = Solution()
   out = test.numDistinct(S, T)
   print out


