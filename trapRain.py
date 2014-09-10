# Given n non-negative integers representing an elevation map where the width of each bar is 1, # compute how much water it is able to trap after raining.

# For example, 
# Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.

class Solution:
    # @param A, a list of integers
    # @return an integer
    def trap(self, A):
       l = len(A)
       if l < 3: return 0
       leftMax, rightMax, area = A[0], A[l-1] , 0
       right = []
       for j in range(1, l-1):
          rightMax = max(rightMax, A[l-1-j])
          right.append(rightMax)
       for i in range(1, l-1):
          leftMax = max(leftMax, A[i-1])
          area += max(0, min(leftMax, right[-i])-A[i])
       print right, leftMax
       return area          

if __name__ == '__main__':
   A = [0,1,0,2,1,0,1,3,2,1,2,1]  
   B = [2,0,2]
   test = Solution()
   out = test.trap(B)
   print out
