# Given a 2D binary matrix filled with 0's and 1's, 
# find the largest rectangle containing all ones and return its area.

class Solution:
    # @param matrix, a list of lists of 1 length string
    # @return an integer
    def maximalRectangle(self, matrix):
        if matrix == []: return 0
        m = len(matrix)
        n = len(matrix[0])
        height = [[0]*(n+1) for i in range(m)]
        maxarea, area = 0, 0
        index = []
        for i in range(m):
            matrix[i].append('0')
            index = []
            for j in range(n+1):
                if matrix[i][j] == '1':
                   height[i][j] = 1+height[i-1][j] if i>0 else 1
                while index != [] and height[i][j] < height[i][index[-1]]:
                    curr = index.pop()
                    area = height[i][curr]*(j-index[-1]-1) if index!=[] else height[i][curr]*j
                    maxarea = max(maxarea, area)
                index.append(j)
        return maxarea

if __name__ == '__main__':
   matrix = [['0','1','1','0','1'],
             ['1','1','0','1','0'],
             ['0','1','1','1','0'],
             ['1','1','1','1','0'],
             ['1','1','1','1','1'],
             ['0','0','0','0','0']]
   test = Solution()
   out = test.maximalRectangle(matrix)
   print out
