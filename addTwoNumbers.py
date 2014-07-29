# You are given two linked lists representing two non-negative numbers. 
# The digits are stored in reverse order 
# and each of their nodes contain a single digit. 
# Add the two numbers and return it as a linked list.

# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8

#Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def addTwoNumbers(l1, l2):
    l3 = ListNode(0)
    out = l3
    add = 0
    
    while l1 != None or l2 != None:
        if l1 == None:
            sumi = add + l2.val
            l2 = l2.next
        elif l2 == None:
            sumi = add + l1.val
            l1 = l1.next
        else: 
            sumi = add + l1.val + l2.val
            l1, l2 = l1.next, l2.next
        
        if sumi >= 10:
            l3.next = ListNode(sumi%10)
            add = 1 
        else:
            l3.next = ListNode(sumi)
            add = 0
        l3 = l3.next
        
    if l1 == None and l2 == None and add == 1:
        l3.next = ListNode(1)
        
    return out.next
    
if __name__ == '__main__':
    l1 = ListNode(9)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)
    
    l2 = ListNode(9)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)
    
    out = addTwoNumbers(l1, l2)