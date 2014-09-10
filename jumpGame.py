# Given an array of non-negative integers, you are initially positioned at the first index of the array.
# Each element in the array represents your maximum jump length at that position.
# Determine if you are able to reach the last index.

# For example:
# A = [2,3,1,1,4], return true.
# A = [3,2,1,0,4], return false.

class Solution:
    # @param A, a list of integers
    # @return a boolean
    def canJump(self, A):
        if A == [0]: return True
        for i in range(len(A)):
            if A[i] == 0: 
               if i != len(A) -1 and self.decide(A, i) == False:
                  return False
        return True

    def decide(self, A, loc): # A[loc] == 0
        for j in range(loc):
            if A[j] > loc - j: return True
        return False
        
if __name__ == '__main__':
   A = [2,3,1,1,4]
   B = [3,2,1,0,4]

   test = Solution()
   out = test.canJump(B)
   print out
   
