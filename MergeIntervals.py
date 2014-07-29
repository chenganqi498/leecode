# Given a collection of intervals, merge all overlapping intervals.
# For example,
# Given [1,3],[2,6],[8,10],[15,18],
# return [1,6],[8,10],[15,18].

class Interval:
     def __init__(self, s=0, e=0):
         self.start = s
         self.end = e
         
def merge(intervals):   
    if len(intervals) <= 1:
        return intervals
        
    record = []
    l = 0
    intervals.sort(key = lambda x: x.start)   
    
    for i in range(1, len(intervals)):
        if intervals[i].start <= intervals[i-1].end:
            intervals[i].end = max(intervals[i].end, intervals[i-1].end)
            l += 1
        else: 
            record.append([i-1, l])
            l = 0
    record.append([i, l])
       
    new = []
    for j in record: 
        new.append(Interval(intervals[j[0]-j[1]].start, intervals[j[0]].end))
    
    return new
    
if __name__ == '__main__':
    intervals = [Interval(2,3), Interval(4,5), Interval(6,7), Interval(8,9), Interval(1,10)]
    out = merge(intervals)
    
        
          
            
    
    
