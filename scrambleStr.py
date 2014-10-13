# Given a string s1, we may represent it as a binary tree 
# by partitioning it to two non-empty substrings recursively.

# Below is one possible representation of s1 = "great":
#     great
#    /    \
#   gr    eat
#  / \    /  \
# g   r  e   at
#            / \
#           a   t

# To scramble the string, we may choose any non-leaf node and swap its two children.

# For example, if we choose the node "gr" and swap its two children, 
# it produces a scrambled string "rgeat".

#     rgeat
#    /    \
#   rg    eat
#  / \    /  \
# r   g  e   at
#            / \
#           a   t
# We say that "rgeat" is a scrambled string of "great".

# Similarly, if we continue to swap the children of nodes "eat" and "at", 
# it produces a scrambled string "rgtae".

#     rgtae
#    /    \
#   rg    tae
#  / \    /  \
# r   g  ta  e
#        / \
#       t   a
# We say that "rgtae" is a scrambled string of "great".

# Given two strings s1 and s2 of the same length, 
# determine if s2 is a scrambled string of s1.

class TreeNode:
    def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

# results[k][i][j]: 
# k: length of substring-1
# i: start position of s1
# j: start position of s2

class Solution:
    # @return a boolean
    def isScramble(self, s1, s2):
        l1, l2 = len(s1), len(s2)
        if l1 != l2: return False
        if l1 == '': return True

        results = [[[False]*l1 for i in range(l1)] for j in range(l1)]
        for i in range(l1):
            for j in range(l2):
                results[0][i][j] = s1[i] == s2[j]

        for k in range(1, l1):
            for i in range(l1-k):
                for j in range(l2-k):
                    for m in range(k):
                         r = (results[m][i][j] and results[k-m-1][i+m+1][j+m+1]) or\
                             (results[m][i][j+k-m] and results[k-m-1][i+m+1][j])
                         if r == True: 
                            results[k][i][j] = True
                            break
        return results[l1-1][0][0]

if __name__ == '__main__':
   s1 = "great"
   s2 = "rgtae"

   test = Solution()
   out = test.isScramble(s1, s2)
   print out


