#According to the Wikipedia's article: "The Game of Life, also known simply as Life, 
#is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

#Given a board with m by n cells, each cell has an initial state live (1) or dead (0). 
#Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

    # Any live cell with fewer than two live neighbors dies, as if caused by under-population.
    # Any live cell with two or three live neighbors lives on to the next generation.
    # Any live cell with more than three live neighbors dies, as if by over-population..
    # Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

#Write a function to compute the next state (after one update) of the board given its current state.

#Follow up:

    # Could you solve it in-place? Remember that the board needs to be updated at the same time: You cannot update some cells first and then use their updated values to update other cells.
    # In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems when the active area encroaches the border of the array. How would you address these problems?

class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        self.m = len(board)
        if self.m == 0: return 
        self.n = len(board[0])
        live, dead = [], []
        
        for i in range(self.m):
            for j in range(self.n):
                liveneib, deadneib = self.neighbors(board, i, j)
                if board[i][j] == 1:
                    if liveneib < 2 or liveneib > 3: 
                        dead.append((i,j))
                    else:
                        live.append((i,j))
                elif liveneib == 3:
                    live.append((i,j))
                    
        for (i,j) in live:
            board[i][j] = 1
        for (i,j) in dead:
            board[i][j] = 0
        
    def neighbors(self, board, i, j):
        neibs = []
        if i != 0:
           neibs.append(board[i-1][j])
           if j != 0:
               neibs.append(board[i-1][j-1])
           if j != self.n-1:
               neibs.append(board[i-1][j+1])
        if i != self.m-1:
            neibs.append(board[i+1][j])
            if j != 0:
                neibs.append(board[i+1][j-1])
            if j != self.n-1:
                neibs.append(board[i+1][j+1])
        if j != 0:
            neibs.append(board[i][j-1])
        if j != self.n-1:
            neibs.append(board[i][j+1])
        livecount = sum(neibs)
        deadcount = len(neibs)-sum(neibs)
        return (livecount, deadcount)
            
        