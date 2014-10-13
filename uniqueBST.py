# Given n, how many structurally unique BST's (binary search trees) 
# that store values 1...n?

# For example,
# Given n = 3, there are a total of 5 unique BST's.

#   1         3     3      2      1
#    \       /     /      / \      \
#     3     2     1      1   3      2
#    /     /       \                 \
#   2     1         2                 3

# exceed time limit
class Solution:
    # @return an integer
    def numTrees(self, n):
        if n <= 1: return 1
        num = [0]*(n+1)
        num[0], num[1] = 1,1
        for i in range(2,n+1):
            for j in range(i):
                num[i] += num[j]*num[i-j-1]
        return num[n]

if __name__ == '__main__':
   test = Solution()
   out = test.numTrees(5)
   print out


