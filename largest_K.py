import heapq

def heapSearch(lt, k):
    heap = []
    
    for i in lt:
        if len(heap) < k:
            heapq.heappush(heap, i)
        
        if heap[0] < i:
            heapq.heappop(heap)
            heapq.heappush(heap, i)
        
    return heap
    
if __name__ == '__main__':
    lt = [1,3,2,4,6,4,7,8,56,23,54,32,11,99]
    print heapSearch(lt, 4)
        
    