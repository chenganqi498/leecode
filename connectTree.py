# Given a binary tree
# Populate each next pointer to point to its next right node. 
# If there is no next right node, the next pointer should be set to NULL.
# Initially, all next pointers are set to NULL.

# Note:
# You may only use constant extra space.
# You may assume that it is a perfect binary tree 
# (ie, all leaves are at the same level, and every parent has two children).

# For example,
# Given the following perfect binary tree,
#         1
#       /  \
#      2    3
#     / \  / \
#    4  5  6  7
# After calling your function, the tree should look like:
#         1 -> NULL
#       /  \
#      2 -> 3 -> NULL
#     / \  / \
#    4->5->6->7 -> NULL

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

def connect(root):
    if root == None or root.left == None:
        return
    root.left.next = root.right
    if root.next != None:
        root.right.next = root.next.left
    connect(root.left)
    connect(root.right)
    
if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right = TreeNode(3)
    root.right.left = TreeNode(6)
    root.right.right =TreeNode(7)

    connect(root) 
     
    

    