# Given a 2D matrix matrix, 
# find the sum of the elements inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).

# Range Sum Query 2D
# The above rectangle (with the red border) is defined by (row1, col1) = (2, 1) and (row2, col2) = (4, 3), which contains sum = 8.

# Example:
# Given matrix = [
#   [3, 0, 1, 4, 2],
#   [5, 6, 3, 2, 1],
#   [1, 2, 0, 1, 5],
#   [4, 1, 0, 1, 7],
#   [1, 0, 3, 0, 5]
# ]

# sumRegion(2, 1, 4, 3) -> 8
# sumRegion(1, 1, 2, 2) -> 11
# sumRegion(1, 2, 2, 4) -> 12

class NumMatrix(object):
    def __init__(self, matrix):
        """
        initialize your data structure here.
        :type matrix: List[List[int]]
        """
        if len(matrix) == 0: m, n = 0, 0
        else: m, n  = len(matrix), len(matrix[0])
        self.sums = [[0]*(n+1) for k in range(m+1)]
        for i in range(m):
            self.sums[i+1][1] = self.sums[i][1]+matrix[i][0]
            for j in range(1, n):
                self.sums[i+1][j+1] = self.sums[i+1][j]+self.sums[i][j+1]-self.sums[i][j]+matrix[i][j]

    def sumRegion(self, row1, col1, row2, col2):
        """
        sum of elements matrix[(row1,col1)..(row2,col2)], inclusive.
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        return self.sums[row2+1][col2+1]-self.sums[row1][col2+1]-self.sums[row2+1][col1]+self.sums[row1][col1]
        
        