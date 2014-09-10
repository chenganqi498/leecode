# Follow up for N-Queens problem.

# Now, instead outputting board configurations, 
#return the total number of distinct solutions.

class Solution:
    # @return a list of lists of string
    def totalNQueens(self, n):
        self.solution = []
        for i in range(n):
            self.add(n, [[0],[i]])                
        return len(self.solution) 
    
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
    out = test.totalNQueens(4)