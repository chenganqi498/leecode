# Given a binary tree, 
# return the zigzag level order traversal of its nodes' values. 
# (ie, from left to right, then right to left for the next level and alternate between).

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def zigzagLevelOrder(self, root):
        if root == None: return []
        current = [root]
        direction = -1
        out = []
        
        while current != []:
            out.append([i.val for i in current])
            current = self.nextLevel(current, direction)
            direction *= -1                 
        return out
          
    def nextLevel(self, current, direction):
        nextlevel = []
        if current == None:
            return nextlevel
        
        if direction == 1: # left to right
            for i in range(len(current)-1, -1, -1):
                if current[i].left != None: nextlevel.append(current[i].left)
                if current[i].right != None: nextlevel.append(current[i].right)
        
        if direction == -1: # right to left
            for i in range(len(current)-1, -1, -1):
                if current[i].right != None: nextlevel.append(current[i].right)
                if current[i].left != None: nextlevel.append(current[i].left)
                
        return nextlevel
  
if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)   
    
    test = Solution()
    out = test.zigzagLevelOrder(root)         