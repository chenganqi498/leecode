# Given a m x n matrix, 
# if an element is 0, set its entire row and column to 0. 
# Do it in place.

# @param matrix, a list of lists of integers
# RETURN NOTHING, MODIFY matrix IN PLACE.

def setZeros(matrix):
    m = len(matrix)
    n = len(matrix[0])
    
    rowzero = set()
    colzero = set()
    
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                rowzero.add(i)
                colzero.add(j)
                
    for j in range(n):
        for i in range(m):
            if i in rowzero:
                matrix[i] = [0]*n
            if j in colzero:            
                matrix[i][j] = 0
                            

if __name__ == '__main__':
    B = [[1,2,0],[3,4,0],[6,7,8]]
    setZeros(B)