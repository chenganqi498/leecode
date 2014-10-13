# Given numRows, generate the first numRows of Pascal's triangle.
# For example, given numRows = 5,
# Return

#    [[1],
#    [1,1],
#   [1,2,1],
#  [1,3,3,1],
# [1,4,6,4,1]]

class Solution:
    # @return a list of lists of integers
    def generate(self, numRows):
        triangle = []
        for i in range(numRows):
            new = [1]*(i+1)
            for j in range(1,i):
                new[j] = triangle[i-1][j-1]+triangle[i-1][j]
            triangle.append(new)
        return triangle

if __name__ == '__main__':
   test = Solution()
   out = test.generate(5)
   print out



