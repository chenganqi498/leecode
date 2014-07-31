# Given a binary tree, 
# check whether it is a mirror of itself (ie, symmetric around its center).

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
 
# root.left = root.right
# root.left.left = root.right.right
# root.left.right = root.right.left       
def isSymmetric(root):
    if root == None:
        return True
    return compare(root.left, root.right)
    
def compare(node1, node2):
    if node1 == None and node2 == None:
        return True
    
    if node1 == None and node2 != None or\
       node2 == None and node1 != None:
         return False
           
    left, right = False, False
    if node1.val == node2.val:
        left = compare(node1.left, node2.right)
        right = compare(node1.right, node2.left)
    else: 
        return False
        
    return left and right
    
if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    #root.left.right = TreeNode(4)
    root.right.right = TreeNode(3)
    #root.right.left = TreeNode(4)
    
    out = isSymmetric(root)