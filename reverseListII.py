# Reverse a linked list from position m to n. Do it in-place and in one-pass.

# For example:
# Given 1->2->3->4->5->NULL, m = 2 and n = 4,

# return 1->4->3->2->5->NULL.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @param m, an integer
    # @param n, an integer
    # @return a ListNode
    def reverseBetween(self, head, m, n):
        new, left = head, head
        if m == n: return head
        count = 1
        while count < m:
           if count < m-1: left = left.next
           head = head.next
           count += 1
 
        tail =  head
        while count < n:
           temp = tail.next
           tail.next = temp.next
           temp.next = head
           head = temp
           count += 1 
        if m != 1: 
           left.next = head
           return new
        else: return head

if __name__ == '__main__':
   head = ListNode(1)
   head.next = ListNode(2)
   head.next.next = ListNode(3)
   head.next.next.next = ListNode(4)
   head.next.next.next.next = ListNode(5)

   test = Solution()
   out = test.reverseBetween(head, 1, 5)
   while out != None:
      print out.val
      out = out.next

           
           
