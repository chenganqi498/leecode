# Given s1, s2, s3, 
# find whether s3 is formed by the interleaving of s1 and s2.

# For example,
# Given:
# s1 = "aabcc",
# s2 = "dbbca",
 
# When s3 = "aadbbcbcac", return true.
# When s3 = "aadbbbaccc", return false.

# results[k][i][j]:
# k,i,j are the length of substr (start from 0) of s3, s1, s2

class Solution:
    # @return a boolean
    def isInterleave(self, s1, s2, s3):
        l1, l2, l3 = len(s1), len(s2), len(s3)
        if l3 != l1+l2: return False
        if l3 == 0: return True
        if l1 == 0: return s3 == s2
        if l2 == 0: return s3 == s1
      
        results = [[[False]*(l2+1) for i in range(l1+1)] for k in range(l3+1)]        
        results[0][0][0] = True
        results[1][1][0], results[1][0][1] = s3[0]==s1[0], s3[0]==s2[0]

        for k in range(2, l3+1):
            for i in range(max(0, k-l2), min(l1+1, k+1)):
                    j = k - i 
                    results[k][i][j] = (i==0 and s3[:j]==s2[:j]) or (results[k-1][i-1][j] and s3[k-1]==s1[i-1]) or\
                                       (j==0 and s3[:i]==s1[:i]) or (results[k-1][i][j-1] and s3[k-1]==s2[j-1])
        return results[l3][l1][l2]

if __name__ == '__main__':
   s1 = "aabcc"
   s2 = "dbbca"
   s3 = "aadbbcbcac"
   s4 = 'aadbbbaccc'

   t1 = 'a'
   t2 = 'b'
   t3 = 'aa'
   test = Solution()
   out = test.isInterleave(s1, s2, s4)
   print out
