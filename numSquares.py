# Given a positive integer n, 
# find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) 
# which sum to n.

# For example, given n = 12, return 3 because 12 = 4 + 4 + 4; 
# given n = 13, return 2 because 13 = 4 + 9.

# DFS, time limit exceeded/maximum recursion depth exceeded
class Solution1(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.counter = n
        self.good = {} 
        self.bad = set()      
        self.DFS(n, 1, 0)         
        return self.counter
        
    def DFS(self, n, start, counter):
        print n
        if n == 0: 
            self.counter = min(self.counter, counter)
            return counter
        if n in self.good:
            counter += self.good[n]
            self.counter = min(self.counter, counter)
            return counter
        if n in self.bad or counter >= self.counter: return 
        
        while start*start <= n:
            tol = self.DFS(n-start*start, start, counter+1)
            if tol != None:
                self.good[n] = tol - counter    
            else:  self.bad.add(n)
            start += 1
        return 

# DP, time limit exceeded     
class Solution2(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = {}
        i = 1
        while i*i <= n:
            dp[i*i] = 1
            i += 1
        
        for j in range(1, n+1):
            if j not in dp: dp[j] = j
            i = 1
            while j + i*i <= n:
                if j+i*i not in dp or dp[j+i*i] > dp[j]+1:
                    dp[j+i*i] = dp[j]+1
                i += 1
        return dp[n]
    
        
