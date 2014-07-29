
class Treenode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
def maxHeight(tree):
    if tree == None:
        return 0
    
    lmax = maxHeight(tree.left)
    rmax = maxHeight(tree.right)
    
    return max(lmax, rmax) + 1

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
    
    print maxHeight(tree)