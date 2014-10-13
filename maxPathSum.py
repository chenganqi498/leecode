# Given a binary tree, find the maximum path sum.
# The path may start and end at any node in the tree.

# For example:
# Given the below binary tree,
#       1
#      / \
#     2   3
# Return 6.

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
        self.max = 0
        self.dfs(root)
        return self.max

    def dfs(self, root):
        if root == None: return 0
        left,right = 0, 0
        left += self.dfs(root.left)
        right += self.dfs(root.right)
        temp = max(left, right, 0)
        self.max = max(self.max, temp+root.val, left+right+root.val)
        return temp + root.val

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
