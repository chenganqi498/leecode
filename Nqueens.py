# -*- coding: utf-8 -*-
# The n-queens puzzle is the problem of placing n queens 
# on an n×n chessboard such that no two queens attack each other.

# Given an integer n, return all distinct solutions to the n-queens puzzle.

# Each solution contains a distinct board configuration of the n-queens' placement, 
# where 'Q' and '.' both indicate a queen and an empty space respectively.

class Solution:
    # @return a list of lists of string
    def solveNQueens(self, n):
        self.solution = []
        for i in range(n):
            self.add(n, [[0],[i]])
            
        final = [] 
        for item in self.solution:
           out = []
           for i in range(n):
             out.append('.'*item[1][i]+'Q'+'.'*(n-item[1][i]-1))
           final.append(out)
        return final
    
    def add(self, n, loc):     
        if len(loc[0]) == n:
            self.solution.append(loc) 
            return 
        for j in range(n):
            if self.check(n, loc, j):
                self.add(n, [loc[0]+[len(loc[0])], loc[1]+[j]])           
        return 
    
    def check(self, n, loc, j):  
        if j in loc[1]: 
            return False
        for k in range(len(loc[0])):
            if len(loc[0]) - k == abs(loc[1][k] - j): 
                return False
        return True
        
    
if __name__ == '__main__':
    test = Solution()
    out = test.solveNQueens(4)