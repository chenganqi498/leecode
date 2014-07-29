# Follow up for "Unique Paths":
# Now consider if some obstacles are added to the grids. 
# How many unique paths would there be?
# An obstacle and empty space is marked as 1 and 0 respectively in the grid.

# For example,
# There is one obstacle in the middle of a 3x3 grid as illustrated below.
#[[0,0,0],
# [0,1,0],
# [0,0,0]]
# The total number of unique paths is 2.

def uniquePathsWithObs(Grid):
    m = len(Grid) # row number
    n = len(Grid[0]) # col number
    
    f = [0]* m
    for i in range(m): f[i] = [0]*n 
    
    for i in range(n):
        if Grid[0][i] == 0:
            f[0][i] = 1
        else: break
            
    for j in range(m):
        if Grid[j][0] == 0:
            f[j][0] = 1
        else: break   
       
    f[0][i+1:n] = [0]*(n-i-1)
    for j in range(j+1, m): f[j][0] = 0
    
    for i in range(1, m):
        for j in range(1, n):          
            if Grid[i][j] == 1:
                f[i][j] = 0
            else:
                f[i][j] = f[i][j-1] + f[i-1][j]              
                
    return f[m-1][n-1]

if __name__ == '__main__':
    Grid = [[0,0,0,1,0],\
             [0,1,0,0,0]]
    out =  uniquePathsWithObs(Grid)