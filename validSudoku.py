# Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.

# The Sudoku board could be partially filled, where empty cells are filled with the character '.'.

# Note:
# A valid Sudoku board (partially filled) is not necessarily solvable. 
# Only the filled cells need to be validated.

class Solution:
    # @param board, a 9x9 2D array
    # @return a boolean
    def isValidSudoku(self, board):
        square = [[{} for j in range(3)] for i in range(3)]
        for i in range(9):
            row, col = {}, {}
            for j in range(9):
                if board[i][j] != '.':
                   if board[i][j] not in row: row[board[i][j]] = [i,j]
                   else: return False
                   if board[i][j] not in square[i/3][j/3]:
                      square[i/3][j/3][board[i][j]] = [i,j]
                   else: return False
                if board[j][i] != '.':
                   if board[j][i] not in col: col[board[j][i]] = [j,i]
                   else: return False
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
   print out
