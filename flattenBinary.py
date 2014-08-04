# Given a binary tree, flatten it to a linked list in-place.

# For example, given
#         1
#        / \
#       2   5
#      / \   \
#     3   4   6   
#
# The flattened tree should look like:
#   1
#    \
#     2
#      \
#       3
#        \
#         4
#          \
#           5
#            \
#             6

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return nothing, do it in place
    
    # flatten by pre-order
    def flatten(self, root):
        stk = []
        self.help(root, stk)    
        self.move(root)            
        
    def help(self, root, stk):
        if root == None: return
        if root.right != None:
            stk.append(root.right)
            root.right = None
        if root.left == None and stk != []:
           root.left = stk.pop() 
        self.help(root.left, stk)
    
    # move from left subtree to right subtree 
    def move(self, root): 
        if root == None:
            return
        self.move(root.left)
        root.right = root.left
        root.left = None
            
if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right = TreeNode(5)
    root.right.right = TreeNode(6)
    
    test = Solution()
    test.flatten(root)