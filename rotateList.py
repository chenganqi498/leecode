# Given a list, rotate the list to the right by k places, where k is non-negative.

# For example:
# Given 1->2->3->4->5->NULL and k = 2,
# return 4->5->1->2->3->NULL.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def rotateRight(self, head, k):
        if head == None: return
        new, old = head, head
        count = 1
        while head.next != None:
            head = head.next
            count += 1

        k = k%count
        if k == 0: return old
        head.next = old
        for i in range(count-k):
            new = new.next
            if i == count-k-1: old.next = None
            else: old = old.next
        return new
        
if __name__ == '__main__':
   head = ListNode(1)
   head.next = ListNode(2)
   head.next.next = ListNode(3)
#   head.next.next.next = ListNode(4)
#   head.next.next.next.next = ListNode(5)

   test = Solution()
   out = test.rotateRight(head, 1)
   while out != None:
         print out.val
         out = out.next
   
