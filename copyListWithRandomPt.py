# A linked list is given such that each node contains an additional random pointer 
# which could point to any node in the list or null.

# Return a deep copy of the list.
# Definition for singly-linked list with a random pointer.
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution:
    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head):
        index, pt = {}, {}
        i, j = 0, 0
        new = RandomListNode(0)
        anchor1, anchor2 = new, new
        new, anchor1 = new.next, new.next
        while head != None:
              new = RandomListNode(head.label)
              index[i] = head.random
              pt[head] = i
              newpt[i] = new 
              new, head = new.next, head.next
              i += 1
        while anchor1 != None:
              anchor1.random = newpt[pt[index[j]]]
              anchor1 = anchor1.next
              j += 1
        return anchor2.next





