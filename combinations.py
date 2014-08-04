# Given two integers n and k, 
# return all possible combinations of k numbers out of 1 ... n.

# For example,
# If n = 4 and k = 2, a solution is:
# [[2,4], [3,4], [2,3], [1,2], [1,3], [1,4]]

class Solution:
    # @return a list of lists of integers
    
    # comb(n, k) = comb(n-1, k) * (n-1)
    def combine(self, n, k): # find subsets of length k
        sets = range(1, n+1)
        c0 = [sets[0:k]]
        c1 = []
        
        for i in range(len(sets) - k):
            c1 = []
            for item in c0:
               for j in range(len(item)):
                   new = sorted(item[0:j] + [sets[k+i]] + item[j+1:])
                   if new not in c1:
                      c1.append(new)
            c0 += c1          
            
        return c0
            
if __name__ == '__main__':
    test = Solution()
    out = test.combine(5,2)