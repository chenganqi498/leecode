# Given a m x n grid filled with non-negative numbers, 
# find a path from top left to bottom right 
# which minimizes the sum of all numbers along its path.

# Note: You can only move either down or right at any point in time.

# mini(i,j) returns the minimum sum ending at grid[i][j]
# mini(i,j) = min(mini(i-1,j) + mini(i,j-1)) + grid[i][j]

def minPathSum(grid):
    m = len(grid) # row number
    n = len(grid[0]) # col number
    if m == 0 or n == 0:
        return 0
    
    mini = [0]* m
    for i in range(m): mini[i] = [0]*n 
    
    mini[0][0] = grid[0][0]
    for i in range(1, m):
        mini[i][0] = mini[i-1][0] + grid[i][0]
    for j in range(1, n):
        mini[0][j] = mini[0][j-1] + grid[0][j]
    
    for i in range(1, m):
        for j in range(1, n):
            mini[i][j] = min(mini[i][j-1], mini[i-1][j]) + grid[i][j]         
    return mini[m-1][n-1]
    
if __name__ == '__main__':
    grid = [[1,2,3],[4,5,6],[7,8,9]]
    grid2 = [[1],[2],[3]]
    out = minPathSum(grid)