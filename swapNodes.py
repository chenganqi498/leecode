# Given a linked list, 
# swap every two adjacent nodes and return its head.
# For example, Given 1->2->3->4, you should return the list as 2->1->4->3.

# Your algorithm should use only constant space. 
# You may not modify the values in the list, only nodes itself can be changed.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def swapNodes(head):
    if head == None or head.next == None:
        return head
    else:
        out = head.next
   
    while head != None and head.next!= None:       
        newhead = head.next   
        nextpair = head.next.next
        if nextpair != None and nextpair.next != None: 
           head.next = nextpair.next
        else:
           head.next = nextpair
        newhead.next = head
        head = nextpair
        
    return out   
        
if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    #head.next.next = ListNode(3)
    #head.next.next.next = ListNode(4)
   
    out = swapNodes(head)
    