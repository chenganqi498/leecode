# Write a program to solve a Sudoku puzzle by filling the empty cells.
# Empty cells are indicated by the character '.'.
# You may assume that there will be only one unique solution.

class Solution:
    # @param board, a 9x9 2D array
    # Solve the Sudoku by modifying the input board in-place.
    # Do not return any value.
    def solveSudoku(self, board):
        self.rows, self.cols = [{} for i in range(9)], [{} for i in range(9)]
        self.squares = [[{} for j in range(3)] for i in range(3)]
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.': 
                   self.rows[i][board[i][j]] = [i,j]
                   self.squares[i/3][j/3][board[i][j]] = [i,j]
                if board[j][j] != '.': 
                   self.cols[j][board[i][j]] = [j,i]
        self.solver(0, board)
        return board

    def solver(self, index, board):
        if index > 80: return
        row, col = index/9, index%9
        if board[row][col] != '.': 
           self.solver(index+1, board)
        for val in range(9):
            if self.isValid(row, col, val):
               temp = board[row]
               board[row]= board[row][:col]+str(val)+board[row][col+1:]
               self.rows[row][str(val)] = [row,col]
               self.cols[col][str(val)] = [row, col]
               self.solver(index+1, board)
               del self.rows[row][str(val)]
               del self.cols[col][str(val)]
               board[row] = temp

    def isValid(self, row, col, val):
        if str(val) in self.rows[row] or str(val) in self.cols[col] or\
           str(val) in self.squares[row][col]: 
           return False
        else: return False


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
   out = test.solveSudoku(board)
   print out
