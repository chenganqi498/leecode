# Given n, generate all structurally unique BST's (binary search trees) 
# that store values 1...n.

# For example,
# Given n = 3, your program should return all 5 unique BST's shown below.

#   1         3     3      2      1
#    \       /     /      / \      \
#     3     2     1      1   3      2
#    /     /       \                 \
#   2     1         2                 3

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @return an integer
    def generateTrees(self, n):
        if n == 0: return [None]
        alltrees = []
        for i in range(1,n+1):
            alltrees += self.buildTrees(i, 0, n+1)
        return alltrees

    def buildTrees(self, root, small, large):            
        if large-small == 2: return [TreeNode(root)]
        left, right = [], []
        for j in range(small+1, root): 
            left += self.buildTrees(j, small, root)
        for k in range(root+1, large): 
            right += self.buildTrees(k, root, large) 
        new = []
        if left == []: left = [None]
        if right == []: right = [None]
        for m in left:
            for n in right:
                newtree = TreeNode(root)
                newtree.left, newtree.right = m, n
                new.append(newtree)
        return new
         
if __name__ == '__main__':
   test = Solution()
   out = test.generateTrees(3)


