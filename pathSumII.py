# Given a binary tree and a sum, 
# determine if the tree has a root-to-leaf path 
# such that adding up all the values along the path equals the given sum.

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a list of lists of integers
    def pathSum(self, root, sumi):
        if root == None: return []
        if root.left == None and root.right == None:
            if sumi == root.val: return [[root.val]]
            else: return []
                
        leftsum = self.pathSum(root.left, sumi - root.val)
        for i in range(len(leftsum)):
            leftsum[i] = [root.val] + leftsum[i]
    
        rightsum = self.pathSum(root.right, sumi - root.val)
        for i in range(len(rightsum)):
            rightsum[i] = [root.val] + rightsum[i]
   
        return leftsum + rightsum
    
if __name__ == '__main__':
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.left.left = TreeNode(11)
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(2)
    root.right = TreeNode(8)
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(4)
    root.right.right.right = TreeNode(1)
    root.right.right.left = TreeNode(5)
    
    test = Solution()
    out = test.pathSum(root, 22) 
    print out
