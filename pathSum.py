# Given a binary tree and a sum, 
# determine if the tree has a root-to-leaf path 
# such that adding up all the values along the path equals the given sum.

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
def hasPathSum(root, sumi):
    if root == None:
        return False
    if root.left == None and root.right == None:
        if sumi == root.val:
            return True
        else:
            return False
                 
    leftsum = hasPathSum(root.left, sumi - root.val)
    rightsum = hasPathSum(root.right, sumi - root.val)
    
    return leftsum or rightsum
    
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
    
    out = hasPathSum(root, 22)
