# Given a binary tree containing digits from 0-9 only, 
# each root-to-leaf path could represent a number.
# An example is the root-to-leaf path 1->2->3 which represents the number 123.
# Find the total sum of all root-to-leaf numbers.



class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None
 
def sumNumbers(root):    
    path, sumi = 0, 0
    return sumPath(root, sumi, path)
    
def sumPath(root, sumi, path):   
    if root == None:
        return 0
        
    path = path*10 + root.val
    
    if root.left == None and root.right == None:
        return path
        
    sumleft = sumPath(root.left, sumi, path)   
    sumright = sumPath(root.right, sumi, path)
    
    return sumleft + sumright
    
if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(5)
    root.right = TreeNode(1)
    root.right.right = TreeNode(6)
       
print sumNumbers(root)