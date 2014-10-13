# Given a binary tree, find its minimum depth.

# The minimum depth is the number of nodes along the shortest path 
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
    def minDepth(self, root):
        if root == None: return 0
        left, right = 1, 1
        left += self.minDepth(root.left)
        right += self.minDepth(root.right)
        if left == 1: return right
        if right == 1: return left
        return min(left, right)

if __name__ == '__main__':
   root = TreeNode(1)
   root.left = TreeNode(2)
   test = Solution()
   out = test.minDepth(root)
   print out


