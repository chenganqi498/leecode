# Follow up for problem "Populating Next Right Pointers in Each Node".
# What if the given tree could be any binary tree? 
# Would your previous solution still work?

# Note:
# You may only use constant extra space.
# For example,
# Given the following binary tree,
#         1
#       /  \
#      2    3
#     / \    \
#    4   5    7
# After calling your function, the tree should look like:
#        1 -> NULL
#       /  \
#      2 -> 3 -> NULL
#     / \    \
#    4-> 5 -> 7 -> NULL

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution:
    def connect(self, root):
        if root == None or (root.left == None and root.right == None):
           return
        if root.left != None and root.right == None:
           root.left.next = self.nextRight(root)
        elif root.left == None and root.right != None:
           root.right.next = self.nextRight(root)
        else:
           root.left.next = root.right
           root.right.next = self.nextRight(root)
        # must connect from right, then left !!!
        self.connect(root.right)
        self.connect(root.left)
    
    def nextRight(self, root):
        if root.next == None:
           return
        if root.next.left == None and root.next.right == None: 
           return self.nextRight(root.next)
        if root.next.left != None:
           return root.next.left
        elif root.next.right != None:
           return root.next.right

if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(0)
    root.left.right = TreeNode(7)
    root.right.left = TreeNode(9)
    root.right.right = TreeNode(1)
    root.left.left.left = TreeNode(2)
    root.left.right.left = TreeNode(1)
    root.left.right.right = TreeNode(0)
    root.right.right.left = TreeNode(8)
    root.right.right.right = TreeNode(8)

    test = Solution()
    out = test.connect(root)

    
