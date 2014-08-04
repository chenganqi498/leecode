# Given a sorted linked list, delete all nodes that have duplicate numbers, 
# leaving only distinct numbers from the original list.

# For example,
# Given 1->2->3->3->4->4->5, return 1->2->5.
# Given 1->1->1->2->3, return 2->3.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        
class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):   
        if head == None or head.next == None: return head  
        out = ListNode(0)
        record = out
        count = 1
       
        while head != None:
            if head.next != None and head.val == head.next.val:
                count += 1
            elif count == 1:
                out.next = head
                out = out.next
            else: count = 1      
            head = head.next         
        out.next = None
            
        return record.next
            
       
if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(3)
    head.next.next = ListNode(3)
    #head.next.next.next = ListNode(4)
    #head.next.next.next.next = ListNode(4)
    
    test = Solution()
    out = test.deleteDuplicates(head)
    