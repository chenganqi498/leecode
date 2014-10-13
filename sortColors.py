# Given an array with n objects colored red, white or blue, 
# sort them so that objects of the same color are adjacent, 
# with the colors in the order red, white and blue.

# Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

# Note:
# You are not suppose to use the library's sort function for this problem.

class Solution:
    # @param A a list of integers
    # @return nothing, sort in place
    def sortColors(self, A):
        colors = [0, 0, 0] # number of color objects
        l = len(A)
        for i in range(l):
            for j in range(len(colors)):
                if A[i] == j:
                   sorted = sum(colors[:j+1])
                   if i > sorted-1 and sorted < l:
                      if i > sorted: colors[A[sorted]] -= 1
                      colors[j] += 1
                      A[sorted], A[i] = A[i], A[sorted]

if __name__ == '__main__':
   A = [1,2,0,2,1,1,0,2,0,2,0,1,0] 
   test = Solution()
   test.sortColors(A)
   print A
