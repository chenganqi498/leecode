# Given a binary tree, return the postorder traversal of its nodes' values.

# For example:
# Given binary tree {1,#,2,3},
#   1
#    \
#     2
#    /
#   3
# return [3,2,1].

# Note: Recursive solution is trivial, could you do it iteratively?

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def postorderTraversal(self, root):
        self.out = []
        self.dfs(root)
        return self.out

    def dfs(self, root):
        if root == None: return        
        self.dfs(root.left)
        self.dfs(root.right)
        self.out.append(root.val)
       
if __name__ == '__main__':
   root = TreeNode(1)
   root.right = TreeNode(2)
   root.right.left = TreeNode(3)
   test = Solution()
   out = test.postorderTraversal(root)
   print out



