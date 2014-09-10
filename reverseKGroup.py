# Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.
# If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.
# You may not alter the values in the nodes, only nodes itself may be changed.
# Only constant memory is allowed.

# For example,
# Given this linked list: 1->2->3->4->5
# For k = 2, you should return: 2->1->4->3->5
# For k = 3, you should return: 3->2->1->4->5

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def reverseKGroup(self, head, k):
        [new, tail] = self.reverseK(head, k)
        while tail != None:
          temp = tail
          [head, tail] = self.reverseK(tail.next, k)
          temp.next = head
        return new

    def reverseK(self, head, k):
        if head == None: return [None, None]
        count = 1
        check = head
        while count < k:
           if check.next == None: return [head, None]
           check = check.next
           count += 1

        count = 1           
        new, temp = head, head
        while count < k:
           new = head.next
           head.next = new.next
           new.next = temp
           temp = new      
           count += 1
        return [new, head]

if __name__ == '__main__':
   head = ListNode(1)
   head.next = ListNode(2)
   head.next.next = ListNode(3)
   head.next.next.next = ListNode(4)
   head.next.next.next.next = ListNode(5)

   test = Solution()
   out = test.reverseKGroup(head, 3)
   while out != None:
      print out.val
      out = out.next
