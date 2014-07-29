# Given a sorted linked list, 
# delete all duplicates such that each element appear only once.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
def deleteDuplicates(head):
    new = ListNode(0)
    new.next = head
    
    while head != None and head.next != None:
        if head.val == head.next.val:
            head.next = head.next.next     
        else:
            head = head.next
    
    return new.next
    
if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(1)
    head.next.next = ListNode(1)
    
    out = deleteDuplicates(head)
    