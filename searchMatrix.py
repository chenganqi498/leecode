# Write an efficient algorithm that searches for a value in an m x n matrix. 
# This matrix has the following properties:
# Integers in each row are sorted from left to right.
# The first integer of each row is greater than the last integer of the previous row.

# For example,
# Consider the following matrix:
#[[1,   3,  5,  7],
# [10, 11, 16, 20],
# [23, 30, 34, 50]]
# Given target = 3, return true.

# Total numbers of the matrix = m*n
# The i-th number is at:
# row = i//n
# col = i%n

def searchMatrix(matrix, target):
    if matrix == [] or matrix == [[]]:
        return False
    m = len(matrix)
    n = len(matrix[0])  
      
    return compare(matrix, m, n, [0, m*n], target)

def transfer(num, m,n):
    i = num//n
    j = num%n
    return [i,j]
    
def compare(matrix, m, n, interval, target): 
    if interval[0] == interval[1]:
        return False
    mid = sum(interval)//2
    [i,j] = transfer(mid, m, n)
     
    left, right = False, False
    
    if matrix[i][j] > target:
        leftInt = [interval[0], mid]
        left = compare(matrix, m, n, leftInt, target)
    elif matrix[i][j] < target:
        rightInt = [mid+1, interval[1]]
        right = compare(matrix, m, n, rightInt, target)
    else:
        return True
               
    return left or right

if __name__ == '__main__':
    matrix = [[1, 3,  5,  7], [10, 11, 16, 20], [23, 30, 34, 50]]
    out = searchMatrix(matrix, 16)
    