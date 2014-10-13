# leecode 98, validate binary search tree
class Treenode:
    def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isValidBST(self, tree, small, large):
        if tree == None: return True
        
        if tree.val > small and tree.val < large:
            left = self.isValidBST(tree.left, small, tree.val)
            right = self.isValidBST(tree.right, tree.val, large)
            return (left and right)
            
        else: return False
    
if __name__ == '__main__':
    tree = Treenode(10)
    tree.left = Treenode(9)
    tree.right = Treenode(11)
    tree.left.left = Treenode(8)
    tree.left.right = Treenode(9.5)
    tree.right.right = Treenode(12)
    tree.right.left = Treenode(10.5)
        
    Out = Solution()
    print Out.isValidBST(tree, -float('inf'), float('inf'))
        
            
        
