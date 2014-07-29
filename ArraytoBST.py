# Convert sorted array to height balanced  BST
# Not optimal, need improvement

class Treenode:
    def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None
         
class Solution:
    # @param num, a list of integers
    # @return a tree node
    def sortedArrayToBST(self, num):        
        if len(num) == 0: return
        # find the median of the array, take it as the root
        median = int(len(num)/2)
        root = Treenode(num[median])  
        
        self.buildTree(num, root)    
  
        return root
        
    def buildTree(self, num, root):        
        if len(num) <= 1: # no children
            return 
                
        median = num.index(root.val)   
        
        # if len(num) == 2, only one children
        if median == len(num)-1: # only left children
            root.left = Treenode(num[0])
            return          
        if median == 0: # only right children
            root.right = Treenode(num[1])
            return
                  
        left = num[0:median]
        right = num[median+1:len(num)]
        
        median_left = int(len(left)/2)
        median_right = int(len(right)/2)
        
        root.left = Treenode(left[median_left])
        root.right = Treenode(right[median_right])
        
        self.buildTree(left, root.left)
        self.buildTree(right, root.right)

if __name__ == '__main__':
    lt = [2,3,4,5,6,7,8,9]
    out = Solution()
    tree = out.sortedArrayToBST(lt)      
        
        
        