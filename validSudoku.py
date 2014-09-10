# Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.

# The Sudoku board could be partially filled, where empty cells are filled with the character '.'.

# A partially filled sudoku which is valid.

# Note:
# A valid Sudoku board (partially filled) is not necessarily solvable. 
# Only the filled cells need to be validated.

class Solution:
    # @param board, a 9x9 2D array
    # @return a boolean
    def isValidSudoku(self, board):
        l = 9      
        for i in range(l):
            row, col = {}, {}
            for j in range(l):  
                if board[i][j] != '.':
                    if board[i][j] not in row: row[board[i][j]] = [i,j]
                    else: return False
                    if board[j][i] not in col: col[board[j][i]] = [j,i]
                    else: return False
            
                if i < l-2 and j < l-2:
                    square = {}
                    for m in range(3):
                        for n in range(3):
                           if board[i+m][j+n] != '.':
                              if board[i+m][j+n] not in square:
                                 square[board[i+m][j+n]] = [i+m,j+n]
                              else: return False
                    print square
                                               
        return True

if __name__ == '__main__':
   board = ["..5.....6",\
             "....14...",\
             ".........",\
             ".....92..",\
             "5....2...",\
             ".......3.",\
             "...54....",\
             "3.....42.",\
             "...27.6.."]
            
   test = Solution()
   out = test.isValidSudoku(board)
#print out
