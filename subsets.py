# Given a set of distinct integers, S, return all possible subsets.

# Note:
# Elements in a subset must be in non-descending order.
# The solution set must not contain duplicate subsets.
# For example,
# If S = [1,2,3], a solution is:
# [[3], [1], [2], [1,2,3], [1,3], [2,3], [1,2], []]
class Solution:
    # @param S, a list of integer
    # @return a list of lists of integer
    def subsets(self, S):
        out = []
        for i in range(len(S)+1):
            out += self.combine(S, i)
        return out
    
    def combine(self, sets, k): # find subsets of length k
        c0 = [sorted(sets[0:k])]
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
    out = test.subsets([4,1,0])