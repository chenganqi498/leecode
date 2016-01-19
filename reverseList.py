#Reverse a singly linked list.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def reverseList(self, head):
        v = []
        while head != None:
            v.append(head.val)
            head = head.next
            
        head  = ListNode(0)
        new = head
        for val in v[::-1]:
            head.next = ListNode(val)
            head = head.next
        return new.next
         