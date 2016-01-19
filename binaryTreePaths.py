#Given a binary tree, return all root-to-leaf paths.

#For example, given the following binary tree:

#   1
# /   \
#2     3
# \
#  5
#All root-to-leaf paths are:

#["1->2->5", "1->3"]

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        self.paths = []
        self.DFS([], root)
        return map(lambda x:'->'.join(x), self.paths)
        
    def DFS(self, path, root):
        if root == None: return
        path += str(root.val),
        if root.left==None and root.right==None:
            self.paths.append(path)
            return
        pathleft, pathright = path[:], path[:]
        if root.left != None: self.DFS(pathleft, root.left)
        if root.right != None: self.DFS(pathright, root.right)
        return