# Given a complete binary tree, count the number of nodes.

# Definition of a complete binary tree from Wikipedia:
# In a complete binary tree every level, except possibly the last, 
# is completely filled, and all nodes in the last level are as far left as possible. 
# It can have between 1 and 2h nodes inclusive at the last level h.

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# BFS, time limit exceed
class Solution1(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None: return 0
        children = [root]     
        level = 0
        nodes = 0
        
        while len(children) == 2**level:
            level += 1
            nodes += len(children)
            children = self.BFS(children)
        nodes += len(children)
        return nodes
        
    def BFS(self, roots):
        children = []
        for i in roots:
            if i.left != None:
               children.append(i.left)
            if i.right != None:
               children.append(i.right)
        return children

# DFS, time limit exceed        
class Solution2(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.count = 0
        self.DFS(root)
        return self.count
        
    def DFS(self, root):
        if root == None: return
        self.count += 1
        self.DFS(root.left)
        self.DFS(root.right)

class Solution3(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None: return 0
        left = self.getHeight(root, 'L')
        right = self.getHeight(root, 'R')
        if left == right: return 2**left -1     
        else: return self.countNodes(root.left)+ self.countNodes(root.right) +1
        
    def getHeight(self, root, direction):
        h = 0
        while root != None:
            if direction == 'L': root = root.left
            else: root = root.right
            h += 1         
        return h
            