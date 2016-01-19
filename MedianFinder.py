# Median is the middle value in an ordered integer list. 
# If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.

# Examples: 
# [2,3,4] , the median is 3

# [2,3], the median is (2 + 3) / 2 = 2.5

# Design a data structure that supports the following two operations:

# void addNum(int num) - Add a integer number from the data stream to the data structure.
# double findMedian() - Return the median of all elements so far.

import heapq as hp

class MedianFinder:
    def __init__(self):
        """
        Initialize your data structure here.
        """ 
        self.left, self.right = [], []

    def addNum(self, num):
        """
        Adds a num into the data structure.
        :type num: int
        :rtype: void
        """
        if len(self.left) == 0 or num < -self.left[0]:
            hp.heappush(self.left, -num)             
        else: 
            hp.heappush(self.right, num)
          
        if len(self.right) > len(self.left): 
               hp.heappush(self.left, -hp.heappop(self.right))
        elif len(self.right) < len(self.left)-1:
               hp.heappush(self.right, -hp.heappop(self.left))
             
    def findMedian(self):
        """
        Returns the median of current data stream
        :rtype: float
        """
        if len(self.left) == 0: return
        if len(self.right) == len(self.left):
            return (self.right[0]-self.left[0])/2.0
        else: 
            return -self.left[0]
            
# Your MedianFinder object will be instantiated and called as such:
# mf = MedianFinder()
# mf.addNum(1)
# mf.findMedian()