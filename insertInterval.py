# Given a set of non-overlapping intervals, 
# insert a new interval into the intervals (merge if necessary).
# You may assume that the intervals were initially sorted according to their start times.

class Interval:
     def __init__(self, s=0, e=0):
         self.start = s
         self.end = e
         
def insert(intervals, newInterval):
    temp = []
    loc = 0
    for i in intervals:     
        if newInterval.start > i.start:
            loc += 1                 
        if overlap(i, newInterval):
            newInterval = \
            Interval(min(i.start, newInterval.start), max(i.end, newInterval.end))         
            temp.append(i)     
        
    intervals.insert(loc, newInterval)   
    
    if temp != []:
       for i in temp:
          intervals.remove(i)                    
    return intervals
  
def overlap(int1, int2):
    if (int2.start >= int1.start and int2.start <= int1.end) or \
       (int1.start >= int2.start and int1.start <= int2.end):
           return True
    else: 
           return False
    
if __name__ == '__main__':
    intervals = [Interval(1,2), Interval(3,5), Interval(6,7), Interval(8,10),\
                 Interval(12, 16)]
    newInterval = Interval(4,9)

    ints2 = [Interval(1,5)]
    new = Interval(5,7)
    insert(ints2, new)