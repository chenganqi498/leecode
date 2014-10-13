# Two elements of a binary search tree (BST) are swapped by mistake.
# Recover the tree without changing its structure.
# Note:
# A solution using O(n) space is pretty straight forward. 
# Could you devise a constant space solution?
# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return a tree node
    def recoverTree(self, root):
        self.n1, self.n2, self.pre = None, None, None
        self.findMistake(root)
        self.n1.val, self.n2.val = self.n2.val, self.n1.val
        return root

    def findMistake(self, root):
        if root == None: return
        self.findMistake(root.left)
        if self.pre and root.val < self.pre.val:
           if self.n1 == None:
              self.n1, self.n2 = self.pre, root
           else:
              self.n2 = root
        self.pre = root
        self.findMistake(root.right)

if __name__ == '__main__':
   root = TreeNode(3)
   root.right = TreeNode(2)
   root.right.right = TreeNode(1)

   test = Solution()
   out = test.recoverTree(root)
   print out.val, out.right.val, out.right.right.val


