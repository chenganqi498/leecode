# Merge k sorted linked lists and return it as one sorted list. 
# Analyze and describe its complexity.
import heapq   
            
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
 
def mergeKLists(lists):
    new = ListNode(0)
    out = new
    recorder = {}
    heap = []
    for i in range(len(lists)):
        if lists[i] != None:
           recorder[lists[i].val] = i
           heapq.heappush(heap, lists[i].val)
  
    while recorder != {}:   
       index = recorder[heap[0]] 
       new.next = lists[index]
       del recorder[heap[0]]
       heapq.heappop(heap)
       
       if lists[index].next != None:                
          lists[index] = lists[index].next
          recorder[lists[index].val] = index   
          heapq.heappush(heap, lists[index].val)    
       new = new.next            
    return out.next

if __name__ == '__main__':
    l1 = ListNode(1)
    l1.next = ListNode(6)
    
    l2 = ListNode(2)
    l2.next = ListNode(4)
    l2.next.next = ListNode(5)
    
    l3 = ListNode(3)
    l3.next = ListNode(7)
    
    lists = [None, l1]   
    out = mergeKLists(lists)