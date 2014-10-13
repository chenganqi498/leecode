# Given a singly linked list L: L0->L1->...->Ln-1->Ln,
# reorder it to: L ->Ln->L->Ln-1->L2->Ln-2...

# You must do this in-place without altering the nodes' values.

# For example,
# Given {1,2,3,4}, reorder it to {1,4,2,3}.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return nothing
    def reorderList(self, head):
        if head == None: return head
        record = {}
        index = 0 
        while head != None:
              record[index] = head
              index += 1
              head = head.next
        record[index/2].next = None
        for i in range((index-1)/2):
            temp = record[i].next
            record[i].next = record[index-1-i]
            record[index-1-i].next = temp
        return record[0]

if __name__ == '__main__':
   head = ListNode(1)
   head.next = ListNode(2)
   #head.next.next = ListNode(3)
   #head.next.next.next = ListNode(4)
   #head.next.next.next.next = ListNode(5)
   
   test = Solution()  
   out = test.reorderList(head) 
   while out != None:
         print out.val
         out = out.next   
