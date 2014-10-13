# Given a binary tree, find its maximum depth.

# The maximum depth is the number of nodes along the longest path 
# from the root node down to the farthest leaf node.

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def maxDepth(self, root):
        if root == None: return 0
        left, right = 1, 1
        left += self.maxDepth(root.left)
        right += self.maxDepth(root.right)
        return max(left, right)

if __name__ == '__main__':
   root = TreeNode(1)
   root.left = TreeNode(2)
   root.right = TreeNode(3)
   root.left.left = TreeNode(4)
   test = Solution()
   out = test.maxDepth(root)
   print out


