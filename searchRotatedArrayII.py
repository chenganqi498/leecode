# Follow up for "Search in Rotated Sorted Array":
# What if duplicates are allowed?

# Would this affect the run-time complexity? How and why?

# Write a function to determine if a given target is in the array.

class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return an integer
    def search(self, A, target):  
        l = len(A)
        median = l//2
        
        if l == 0: return False   
        if target == A[0]: return True      
        if target == A[median]: return True
        
        if target > A[0]: # in the large part    
            if target < A[median] or A[0] > A[median]:
                exist = self.search(A[:median], target)
            elif A[0] == A[median] and A[0] == A[-1]:
                exist = self.search(A[:median], target) or\
                        self.search(A[median+1:], target)            
            else: 
                exist  = self.search(A[median+1:], target)                                  
        else: # in the small part
            if target > A[median] or A[-1] < A[median]:
                exist = self.search(A[median+1:], target)
            elif A[-1] == A[median] and A[median] == A[0]:
                exist = self.search(A[:median], target) or\
                        self.search(A[median+1:], target)      
            else:
                exist = self.search(A[:median], target)
      
        return exist
        
if __name__ == '__main__':
    A = [1,1,3,1]
    test = Solution()
    out = test.search(A, 3) 