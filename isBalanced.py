class Treenode:
    def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None
         
def isBalanced(tree):
    if tree == None:
        return True
    
    if abs(treeDepth(tree.left) - treeDepth(tree.right)) <= 1:
        left = isBalanced(tree.left)
        right = isBalanced(tree.right)
        return left and right
    else: 
        return False

def treeDepth(tree):
    if tree == None:
        return 0
    lmax = treeDepth(tree.left)
    rmax = treeDepth(tree.right)
    
    return max(lmax, rmax) + 1
    
if __name__ == '__main__':
    tree = Treenode(10)
    tree.left = Treenode(9)
    tree.left.left = Treenode(8)
    tree.right = Treenode(12)
    tree.right.right = Treenode(30)
    tree.right.right.right = Treenode(0)

print isBalanced(tree)