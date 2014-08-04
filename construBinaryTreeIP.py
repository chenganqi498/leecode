# Given inorder and postorder traversal of a tree, construct the binary tree.

# Note:
# You may assume that duplicates do not exist in the tree.

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param inorder, a list of integers
    # @param postorder, a list of integers
    # @return a tree node
    def buildTree(self, inorder, postorder):
        if postorder == []  or inorder == []:
            return None  
        root = TreeNode(postorder[-1])
        loc = inorder.index(root.val)
        
        leftIn, rightIn = inorder[:loc], inorder[loc+1:]             
        if leftIn != [] and rightIn != []:
           for i in range(len(postorder)-2):
               if postorder[i] in leftIn and postorder[i+1] in rightIn:
                   sep = i+1
                   break
        elif leftIn == []: sep = 0
        elif rightIn == []: sep = len(postorder)-1 
        leftPost, rightPost = postorder[0:sep], postorder[sep:-1]
        
        root.left = self.buildTree(leftIn, leftPost)
        root.right = self.buildTree(rightIn, rightPost)
        
        return root
        
if __name__ == '__main__':
    inorder = ['A','B','C','D','E','F','G','H','I']
    postorder = ['A','C','E','D','B','H','I','G','F']
    
    test = Solution()
    out = test.buildTree(inorder, postorder)