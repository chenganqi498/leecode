# Suppose a sorted array is rotated at some pivot unknown to you beforehand.
# (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

# You are given a target value to search. 
# If found in the array return its index, otherwise return -1.

# You may assume no duplicate exists in the array.

class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return an integer
    def search(self, A, target):  
        l = len(A)
        median = l//2
        
        if l == 0: return -1      
        if target == A[0]: return 0        
        if target == A[median]: return median
                
        if target > A[0]: # in the large part    
            if target < A[median] or A[0] > A[median]:
                index = self.search(A[:median], target)
            else: 
                shift  = self.search(A[median+1:], target)
                index = -1 if shift == -1 else median + shift + 1                        
        else: # in the small part
            if target > A[median] or A[-1] < A[median]:
                shift = self.search(A[median+1:], target)
                index = -1 if shift == -1 else median + shift + 1
            else:
                index = self.search(A[:median], target)
      
        return index
            
            
if __name__ == '__main__':
    A = [4,5,6,8,0,1,2]
    test = Solution()
    out = test.search(A, 7) 
    