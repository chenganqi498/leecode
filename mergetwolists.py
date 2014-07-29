# Merge two sorted singly linked lists

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param two ListNodes
    # @return a ListNode
    def mergeTwoLists(self, l1, l2):
        new = ListNode(0)
        back = new
          
        while l1 != None or l2 != None:
          if l1 == None or l1.val > l2.val:
              new.next, l2 =  l2, l2.next
        
          elif l2 == None or l1.val < l2.val:
              new.next, l1 = l1, l1.next
          
          new = new.next
        # the first node is set by hand, so drop it
        return back.next
        
if __name__ == '__main__':
    l1 = ListNode(1)
    l1.next = ListNode(3)
    l2 = ListNode(2)
    # l2.next = ListNode(4)
    
    sol = Solution()
    pp = sol.mergeTwoLists(l1, l2)
    