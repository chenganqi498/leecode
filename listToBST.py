# Given a singly linked list where elements are sorted in ascending order, 
# convert it to a height balanced BST.

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a list node
    # @return a tree node
    def sortedListToBST(self, head):
        heads = []     
        while head != None:
            heads.append(head)
            head = head.next
     
        return self.buildTree(heads)
      
    def buildTree(self, heads):  
        if heads == []: return
        median = len(heads)//2    
        root = TreeNode(heads[median].val)       
        root.left = self.buildTree(heads[:median])
        root.right = self.buildTree(heads[median+1:])
        
        return root
        
if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(4)
    head.next.next.next = ListNode(5)
    
    test = Solution()
    out = test.sortedListToBST(head)  
        