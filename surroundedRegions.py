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

# This verison exceeds time limit on big data test
class Solution:
    # @param board, a 2D array
    # Capture all regions by modifying the input board in-place.
    # Do not return any value.
    def solve(self, board):
        if board == []: return []
        visited = []
        change = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O':
                    if [i,j] not in visited:
                        visited.append([i,j])
                        self.count = 1
                        if self.checkNeighbor(board, i, j, visited):                    
                            change += visited[len(visited)-self.count:]
                           
        for item in change:
            board[item[0]][item[1]] = 'X'
        
    def checkNeighbor(self, board, i, j, visited):
        # hit boundary
        if i == 0 or i == len(board) - 1 or j == 0 or j == len(board[0])-1:
            return False
            
        neighbors = [True, True, True, True] # left, right, up, down
        directions = [[i, j-1], [i, j+1], [i-1, j], [i+1, j]]
        
        for i in range(len(directions)):
            if directions[i] not in visited and board[directions[i][0]][directions[i][1]] == 'O':
                visited.append(directions[i])
                self.count += 1
                neighbors[i] = self.checkNeighbor(board, directions[i][0], directions[i][1], visited)     
        
        return neighbors[0] and neighbors[1] and neighbors[2] and neighbors[3]
        
        
if __name__ == '__main__':
    board = [['X', 'X', 'X', 'X'], \
             ['X', 'O', 'O', 'X'], \
             ['X', 'X', 'O', 'X'], \
             ['X', 'O', 'X', 'X']]
             
    test = Solution()
    out = test.solve(board)
            