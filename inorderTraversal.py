# Given a binary tree, 
# return the inorder traversal of its nodes' values.
# For example:
# Given binary tree {1,#,2,3},
#   1
#    \
#     2
#    /
#  3
# return [1,3,2].
# Note: Recursive solution is trivial, could you do it iteratively?

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
def inorderTraversal(root):
    values = []
    addNode(root, values)
    
    return values
    
def addNode(node, values):
    if node == None:
        return
    addNode(node.left, values)
    values.append(node.val)   
    addNode(node.right, values)    
    
if __name__ == '__main__':
    root = TreeNode('F')
    root.left = TreeNode('B')
    root.left.left = TreeNode('A')
    root.left.right = TreeNode('D')
    root.left.right.left = TreeNode('C')
    root.left.right.right = TreeNode('E')
    root.right = TreeNode('G')
    root.right.right = TreeNode('I')
    root.right.right.left = TreeNode('H')
   
    out = inorderTraversal(root) 
    
