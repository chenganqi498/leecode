def spiral(A):
    if A == []:
        return A
    
    row = len(A)
    col = len(A[0])   
    i, j, k = 0, 0, 0
    out = [] 
    dx, dy = 0, 1 # direction vector
      
    for counter in range(row*col):
        
        if row - 2*k == 1:
            dx, dy =  0, 1
        elif col - 2*k == 1:
            dx, dy = 1, 0                         
        # topright corner
        if i == k and j == col - 1 - k:
            dx, dy = 1, 0                       
        # bottomright corner
        elif i == row - 1 - k and j == col -1 - k:
            dx, dy = 0, -1                        
        # bottomleft corner
        elif i == row - 1 - k and j == k:
            dx, dy = -1, 0        
        # topleft corner, ATTENTION: different from other three!
        # Because it's not a circal but a spiral, not closed!
        elif i == k + 1 and j == k:
            dx, dy = 0, 1
            k = k+1
         
        print A[i][j] 
        print 'direction', dx, dy
        out.append(A[i][j])
        i += dx
        j += dy
        
        
    return out
 
if __name__ == '__main__':
    A = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    B= [[1],[2],[3]]
    C = [[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15]]
    print spiral(B)
    
               
    