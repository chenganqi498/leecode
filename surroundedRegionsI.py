# Given a 2D board containing 'X' and 'O', capture all regions surrounded by 'X'.
# A region is captured by flipping all 'O's into 'X's in that surrounded region.

# For example,
# X X X X
# X O O X
# X X O X
# X O X X

# After running your function, the board should be:
# X X X X
# X X X X
# X X X X
# X O X X

class Solution:
    # @param board, a 2D array
    # Capture all regions by modifying the input board in-place.
    # Do not return any value.
    def solve(self, board):
        if board == []: return []
        row = len(board)
        col = len(board[0])
        
        left = [[i, 0] for i in range(row)]
        right = [[i, col-1] for i in range(row)]
        up = [[0, j] for j in range(1, col-1)]
        down = [[row-1, j] for j in range(1, col-1)]
        boundary = left + right + up + down
        visited = []
        
        for item in boundary:
            i, j = item[0], item[1]
            if board[i][j] == 'O':
                board[i][j] = 'Y'
                visited.append([i,j])
        
        while visited != []:
            neighbors = []
            for item in visited:
                neighbors += self.checkNeighbor(board, item[0], item[1])                    
            visited = neighbors
            
        for i in range(row):
            for j in range(col):
                if board[i][j] == 'O': board[i][j] = 'X'
                if board[i][j] == 'Y': board[i][j] = 'O'                
                   
    def checkNeighbor(self, board, i, j):
        directions, neighbors = [], []
        if i != 0: directions.append([i-1, j])
        if i != len(board) - 1: directions.append([i+1, j])
        if j != 0: directions.append([i, j-1])
        if j != len(board[0])-1: directions.append([i, j+1])
        
        for item in directions:
            [m,n] = item
            if board[m][n] == 'O':
                board[m][n] = 'Y'
                neighbors.append([m,n])             
        return neighbors    
        
if __name__ == '__main__':
    board = [['X', 'X', 'X', 'X'], \
             ['X', 'O', 'O', 'X'], \
             ['X', 'X', 'O', 'X'], \
             ['X', 'O', 'X', 'X']]
             
    test = Solution()
    out = test.solve(board)