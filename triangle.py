# Given a triangle, find the minimum path sum from top to bottom. 
# Each step you may move to adjacent numbers on the row below.

# For example, given the following triangle
# [   [2],
#    [3,4],
#   [6,5,7],
#  [4,1,8,3]]

# The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).
# Note:
# Bonus point if you are able to do this using only O(n) extra space, 
# where n is the total number of rows in the triangle.

class Solution:
    # @param triangle, a list of lists of integers
    # @return an integer
    def minimumTotal(self, triangle):
        if triangle == []: return 0
        minsum = triangle[-1]
        for i in range(len(triangle)-2, -1, -1):
            temp = []
            for j in range(len(triangle[i])):
                temp.append(triangle[i][j]+min(minsum[j],minsum[j+1]))
            minsum = temp
        return min(minsum)

if __name__ == '__main__':
   triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
   test = Solution()
   out = test.minimumTotal(triangle)
   print out



