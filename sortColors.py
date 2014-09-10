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
        red, white, blue = 0, 0, 0 # number of color objects
        l = len(A)
        for i in range(l):
            print A
            print i, red, white, blue
            if A[i] == 0:
               if i > red-1 and red < l:
                  A[red], A[i] = A[i], A[red]
               red += 1
            if A[i] == 1:
               if i>red+white-1 and red+white < l:
                  A[red+white], A[i] = A[i], A[red+white]   
               if red+white+blue <= i: white += 1
            if A[i] == 2:
               if i>red+white+blue-1 and red+white+blue<l:
                  A[red+white+blue], A[i] = A[i], A[red+white+blue]
               if red+white+blue <= i: blue += 1

if __name__ == '__main__':
   A = [0,2,0,1,0] 
   test = Solution()
   test.sortColors(A)
   print A
