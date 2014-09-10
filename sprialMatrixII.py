# Given an integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

# For example,
# Given n = 3,

# You should return the following matrix:
# [
#  [ 1, 2, 3 ],
#  [ 8, 9, 4 ],
#  [ 7, 6, 5 ]
# ]

class Solution:
    # @return a list of lists of integer
    def generateMatrix(self, n):
        x, y = 0, 0
        dx, dy = 0, 1 # dx in row, dy in col
        k = 0
        A = [[0]*n for i in range(n)]
        for i in range(1, n*n+1):
           A[x][y] = i
           if x == k and y == n-1-k: dx, dy = 1, 0
           elif x == n-1-k and y == n-1-k: dx, dy = 0, -1
           elif x == n-1-k and y == k: dx, dy = -1, 0
           elif x == k+1 and y == k: 
              k += 1
              dx, dy = 0, 1
           x += dx
           y += dy

        return A

if __name__ == '__main__':
   test = Solution()
   out = test.generateMatrix(4)
