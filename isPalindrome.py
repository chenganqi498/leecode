# Given a singly linked list, determine if it is a palindrome.

# Follow up:
# Could you do it in O(n) time and O(1) space?
# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None: return True
        new = ListNode(0)
        new.next = head
        
        record = []
        while head != None:
            record.append(head.val)
            head = head.next
        
        newhead = new.next
        while newhead != None:
            if len(record) <=1: return True
            elif newhead.val != record[-1]: return False
            else:
                record.pop()
                newhead = newhead.next
               