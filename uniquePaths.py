# -*- coding: utf-8 -*-
# A robot is located at the top-left corner of a m x n grid.
# The robot can only move either down or right at any point in time. 
# The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
# How many possible unique paths are there?

# f(i, 0) = f(0, j) = 1
# f(i, j) = f(i-1, j) + f(i, j-1)

def uniquePaths(m, n):
    if m == 1 or n == 1:
        return 1
     
    # Attention: 
    # replicating a list with * doesn’t create copies, 
    # it only creates references to the existing objects
    # Do not create 2d array like: A = [[None] * 2] * 3 !!! 
    f = [0]* m
    for i in range(m): f[i] = [0]*n 
    f[0] = [1]*n
    for i in range(m): f[i][0] = 1
    
    for i in range(1, m):
        for j in range(1, n):
                f[i][j] = f[i-1][j] + f[i][j-1]
           
    return f[m-1][n-1]
    
if __name__ == '__main__':
    out = uniquePaths(2, 3)