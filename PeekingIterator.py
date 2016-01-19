# Given an Iterator class interface with methods: next() and hasNext(), 
# design and implement a PeekingIterator that support the peek() operation -- 
# it essentially peek() at the element that will be returned by the next call to next().

# Here is an example. Assume that the iterator is initialized to the beginning of the list: [1, 2, 3].

# Call next() gets you 1, the first element in the list.

# Now you call peek() and it returns 2, the next element. Calling next() after that still return 2.

# You call next() the final time and it returns 3, the last element. Calling hasNext() after that should return false.

# Below is the interface for Iterator, which is already defined for you.
#
class Iterator(object):
    def __init__(self, nums):
        """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
        self.lt = nums
        self.pt = -1

    def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
        if self.pt == len(self.lt)-1:
            return False
        return True

    def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """
          if self.hasNext() == True:
              self.pt = self.pt+1
          return self.lt[self.pt]
          
class PeekingIterator(object):
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.nums = []
        while iterator.hasNext() == True:
            self.nums.append(iterator.next())
        self.pt = -1
        self.iter = Iterator(self.nums)
            
    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if self.hasNext() == True:
           return self.nums[self.pt+1]
 
        return

    def next(self):
        """
        :rtype: int
        """
        self.pt += 1
        return self.iter.next()

    def hasNext(self):
        return self.iter.hasNext()