class Solution:
    # @param {integer} k
    # @param {integer} n
    # @return {integer[][]}
    def combinationSum3(self, k, n):
        if 9*k < n: return []
        self.out = []
        self.k = k
        i = 1
        while i < 9:
            self.count = 1
            self.my = [i]
            self.out.append(self.DFS(i,n))
            i += 1
        return self.out
            
        
    def DFS(self, i, n):
        n = n - i
        self.count += 1
        if self.count == self.k:
           if n == 0: return [i]
           else: return []
        
        for j in range(i+1, 10):
            out = self.DFS(j, n)
            if out != []: out = [j] + out
        return out
        
out = Solution()
x = out.combinationSum3(3, 7)