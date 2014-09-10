class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverse(self, head):
        tail = head
        while tail.next != None:
          new = tail.next
          tail.next = new.next
          new.next = head
          head = new
        return head

