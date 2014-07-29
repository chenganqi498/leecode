# Binary tree level order
class Treenode:
    def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None
         
class Solution:
    def levelOrder(self, tree):
        if tree is None: 
            return []
        
        tol = [[tree.val]]             
        parents = [tree]
    
        while parents != []:
            current = self.CurrentLevel(parents)
            if current == []:
                break
            
            level = []         
            for i in current:
                level.append(i.val) 
            tol.append(level)
            parents = current
     
        return tol
        
    def CurrentLevel(self, parents):
        current = []
        for node in parents:
            if node.left != None:
              current.append(node.left)
        
            if node.right != None:
              current.append(node.right)
              
        return current
                         
if __name__ == '__main__':
    tree = Treenode(3)
    tree.left = Treenode(9)
    tree.right = Treenode(0)
    tree.right.left = Treenode(15)
    tree.right.right = Treenode(7)
    tree.left.right = Treenode(20)
    tree.left.right.right = Treenode(25)
    tree.left.right.left = Treenode(30)
    tree.left.right.left.right = Treenode(13)
    
    out = Solution()
    #print [tree], level
    print out.levelOrder(tree)
      