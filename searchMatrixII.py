#Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

#    Integers in each row are sorted in ascending from left to right.
#    Integers in each column are sorted in ascending from top to bottom.

#For example,

#Consider the following matrix:

#[
#  [1,   4,  7, 11, 15],
#  [2,   5,  8, 12, 19],
#  [3,   6,  9, 16, 22],
#  [10, 13, 14, 17, 24],
#  [18, 21, 23, 26, 30]
#]

#Given target = 5, return true.

#Given target = 20, return false.

class Solution:
    # @param {integer[][]} matrix
    # @param {integer} target
    # @return {boolean}
    def searchMatrix(self, matrix, target):
        if len(matrix) == 0: return False
        m, n = len(matrix), len(matrix[0])
        rows, cols = [], []
        for i in range(m):
            if target >= matrix[i][0]:
                if target <= matrix[i][-1]:
                    rows.append(i)
        if rows == []: return False
        
        for j in range(n):
            if target >= matrix[0][j]:
                if target <= matrix[-1][j]:
                   cols.append(j)
        if cols == []: return False
        
        for i in rows:
            for j in cols:
                if target == matrix[i][j]: return True
                
        return False