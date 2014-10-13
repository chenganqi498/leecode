# Given a binary tree, find the maximum root-leaf path sum.

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def maxPathSum(self, root):
        if root == None: return 0
        self.max = 0
        self.dfs(root, 0)
        return self.max

    def dfs(self, root, sumi): 
        if root == None: return 0
        sumi += root.val
        self.max = max(self.max, sumi)
        self.dfs(root.left, sumi)
        self.dfs(root.right, sumi)

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(0)
    root.left.right = TreeNode(7)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(1)
    root.left.left.left = TreeNode(2)
    root.left.right.left = TreeNode(1)
    root.left.right.right = TreeNode(0)
    root.right.right.left = TreeNode(8)
    root.right.right.right = TreeNode(8)

    test = Solution()
    out = test.maxPathSum(root)
    print out
