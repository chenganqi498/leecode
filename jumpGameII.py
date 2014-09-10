# Given an array of non-negative integers, you are initially positioned at the first index of the array.
# Each element in the array represents your maximum jump length at that position.
# Your goal is to reach the last index in the minimum number of jumps.

# For example:
# Given array A = [2,3,1,1,4]
# The minimum number of jumps to reach the last index is 2. 
# (Jump 1 step from index 0 to 1, then 3 steps to the last index.)

# exceed time limit on large data set
class Solution:
    # @param A, a list of integers
    # @return a boolean
    def jump(self, A):
        self.minstep = float('inf')
        self.dfs(A, 0, 0)
        return self.minstep

    def dfs(self, A, start, steps):
        l = len(A)
        if start == l-1: 
           self.minstep = min(self.minstep, steps)
           return 
        if A[start] == 0: return

        for i in range(1, A[start]+1):
            if start + i > l-1: return 
            self.dfs(A, start + i, steps+1)
        return
         
if __name__ == '__main__':
   A = [2,3,1,1,4]
   B = [6,2,6,1,7,9,3,5,3,7,2,8,9,4,7,7,2,2,8,4,6,6,1,3]
   test = Solution()
   out = test.jump(B)
   print out
   
