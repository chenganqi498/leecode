# Given a sorted array of integers, 
# find the starting and ending position of a given target value.

# Your algorithm's runtime complexity must be in the order of O(log n).
# If the target is not found in the array, return [-1, -1].

# For example,
# Given [5, 7, 7, 8, 8, 10] and target value 8,
# return [3, 4].

class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return a list of length 2, [index1, index2]
    def searchRange(self, A, target):
        l = len(A)
        median = l//2
        if l == 0: return [-1, -1]
       
        if target > A[median]:
            shift = self.searchRange(A[median+1:], target)
            [lower, upper] = [-1, -1] if -1 in shift \
                             else [shift[0]+median+1, shift[1]+median+1]
        
        elif target < A[median]: 
            shift = self.searchRange(A[:median], target)
            [lower, upper] = [-1, -1] if -1 in shift else shift 
        
        else:
            shift_low = self.searchRange(A[:median], target)[0]
            shift_up = self.searchRange(A[median+1:], target)[1]
            lower = median if shift_low == -1 else shift_low
            upper = median if shift_up == -1 else median + shift_up + 1
            
        return [lower, upper]
        
if __name__ == '__main__':
    A = [5,7,7,8,8,10]
    target = 10
    test = Solution()
    out = test.searchRange(A, target)