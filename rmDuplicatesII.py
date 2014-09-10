# Follow up for "Remove Duplicates":
# What if duplicates are allowed at most twice?

# For example,
# Given sorted array A = [1,1,1,2,2,3],

# Your function should return length = 5, and A is now [1,1,2,2,3].

class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        sz, i = 0, 0
        while i < len(A):
            count = 1
            A[sz] = A[i]
            sz += 1 
            i += 1
            while i < len(A) and A[i-1] == A[i]:
               count += 1
               if count == 2:
                  A[sz] = A[i]
                  sz += 1
               i += 1
        A = A[:sz]
        return  sz
        
if __name__ == '__main__':
  A = [1,1,1,2,2,3]
  test = Solution()
  out = test.removeDuplicates(A)
