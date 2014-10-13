# Given a sorted array and a target value, 
# return the index if the target is found. 
# If not, return the index where it would be if it were inserted in order.

# You may assume no duplicates in the array.

class Solution:
    # @param A, a list of integers
    # @param target, an integer to be inserted
    # @return integer
    def searchInsert(self, A, target):
        if A == []: return 0
        if len(A) == 1: return 1 if target > A[0] else 0
        median = len(A)/2
        if target == A[median]: return median
        elif target > A[median]: 
             index = median + 1+ self.searchInsert(A[median+1:], target)
        else:
             index = self.searchInsert(A[:median], target)
        return index

if __name__ == '__main__':
   A = [1,3,5,6]
   test = Solution()
   out = test.searchInsert(A, 5)
   print out
