# Sort a linked list using insertion sort.

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        newhead = ListNode(0)
        newhead.next = head  
        temphead = newhead
        
        while head != None and head.next != None and temphead != None:
            if temphead.next == head.next:
                head = head.next      
                temphead = newhead        
            elif head.next.val < temphead.next.val:
                temp = head.next
                head.next = head.next.next
                temphead.next = temp
                temp.next = head         
            else: temphead = temphead.next
            
        return newhead.next