# Given an unsorted integer array, find the first missing positive integer.
# For example,
# Given [1,2,0] return 3,
# and [3,4,-1,1] return 2.

# Your algorithm should run in O(n) time and uses constant space.

class Solution:
    # @param A, a list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        l = len(A)
        for i in range(l):
            while A[i]-1 != i and -1 < A[i]-1 < l:
               loc = A[i]-1
               if A[loc] == A[i]: break
               A[loc], A[i] = A[i], A[loc]    
        count = 0
        while count < l and A[count]-1 == count:
            count += 1
        return count+1

if __name__ == '__main__':
   A = [3,4,-1,1]
   test = Solution()
   out = test.firstMissingPositive(A)
   print out

