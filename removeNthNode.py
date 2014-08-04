# Given a linked list, remove the nth node from the end of list and return its head.
# For example,
# Given linked list: 1->2->3->4->5, and n = 2.
# After removing the second node from the end, the linked list becomes 1->2->3->5.
# Note:
# Given n will always be valid.
# Try to do this in one pass.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @return a ListNode
    def removeNthFromEnd(self, head, n):
        head0 = ListNode(0)
        head1 = ListNode(0)
        head0.next = head
        head1.next = head0
        
        for i in range(n-1):
            head = head.next
                 
        while head.next != None:
            head = head.next
            head0 = head0.next
            
        head0.next = head0.next.next        
        return head1.next.next

if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    
    test = Solution()
    out = test.removeNthFromEnd(head, 2)
    