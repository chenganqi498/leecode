# Given a binary tree, imagine yourself standing on the right side of it, 
# return the values of the nodes you can see ordered from top to bottom.

# For example:
# Given the following binary tree,

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def rightSideView(self, root):
        if root == None: return []
        self.out = []
        self.find_right([root])
        return self.out
    def children(self, roots):
        children = []
        for r in roots:
            if r.left != None: children.append(r.left)
            if r.right != None: children.append(r.right)
        return children
    def find_right(self, roots):
        if roots == []: return
        self.out.append(roots[-1].val)
        roots = self.children(roots)
        self.find_right(roots)
        
        