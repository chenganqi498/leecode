# Given preorder and inorder traversal of a tree, construct the binary tree.

# Note:
# You may assume that duplicates do not exist in the tree.

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param preorder, a list of integers
    # @param inorder, a list of integers
    # @return a tree node
    
    # pre-order: root -> left -> right
    # post-order: left -> root -> right
    def buildTree(self, preorder, inorder):
        if preorder == []  or inorder == []:
            return None           
        root = TreeNode(preorder[0])       
        loc = inorder.index(root.val)
               
        leftIn, rightIn = inorder[:loc], inorder[loc+1:]        
        if leftIn != [] and rightIn != []:
           for i in range(len(1, preorder)-1):
               if preorder[i] in leftIn and preorder[i+1] in rightIn:
                   sep = i
                   break
        elif leftIn == []: sep = 0
        elif rightIn == []: sep = len(preorder)       
        leftPre, rightPre = preorder[1:sep+1], preorder[sep+1:]
        
        root.left = self.buildTree(leftPre, leftIn)
        root.right = self.buildTree(rightPre, rightIn)
        
        return root
 
if __name__ == '__main__':
    preorder = ['F','B','A','D','C','E','G','I','H']
    inorder = ['A','B','C','D','E','F','G','H','I']
    
    test = Solution()
    out = test.buildTree(preorder, inorder)