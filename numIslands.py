#Number of Islands Total Accepted: 4863 Total Submissions: 23172

#Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. 
#An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

#Example 1:

#11110
#11010
#11000
#00000

#Answer: 1

#Example 2:

#11000
#11000
#00100
#00011

#Answer: 3

class Solution:
    # @param grid, a list of list of characters
    # @return an integer
    def numIslands(self, grid):
        if grid == []: return 0
        count = 0
        self.m, self.n = len(grid), len(grid[0])
        self.grid = grid
        for i in range(self.m):
            for j in range(self.n):
                if self.grid[i][j] == '1':
                       count += 1
                       self.DFS(i, j)              
        return count
        
    def DFS(self, i, j):
        if i < self.m-1 and self.grid[i+1][j] == '1':
            self.grid[i+1][j] = '2'
            self.DFS(i+1,j)
        if i > 0 and self.grid[i-1][j] == '1':
            self.grid[i-1][j] = '2'
            self.DFS(i-1,j)
        if j < self.n-1 and self.grid[i][j+1] == '1':
            self.grid[i][j+1] = '2'
            self.DFS(i, j+1) 
        if j > 0 and self.grid[i][j-1] == '1':
            self.grid[i][j-1] = '2'  
            self.DFS(i, j-1)     
        return 

if __name__ == '__main__':
    grid = [['1','0','1','1','1'],\
            ['1','0','1','0','1'],\
            ['1','1','1','0','1']]
    x = Solution()
    print x.numIslands(grid)