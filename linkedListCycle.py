# Given a linked list, determine if it has a cycle in it.
# Follow up:
# Can you solve it without using extra space?

#  Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a boolean
    def hasCycle(self, head):
        record = {}
        while head != None:
              record[head] = 0
              if head.next in record: return True
              head = head.next 
        return False

