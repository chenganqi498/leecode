# Given a collection of candidate numbers (C) and a target number (T), 
# find all unique combinations in C where the candidate numbers sums to T.

# Each number in C may only be used once in the combination.

# Note:
# All numbers (including target) will be positive integers.
# Elements in a combination must be in non-descending order. 
# The solution set must not contain duplicate combinations.
# For example, given candidate set 10,1,2,7,6,1,5 and target 8, 
# A solution set is: 
# [1, 7] 
# [1, 2, 5] 
# [2, 6] 
# [1, 1, 6]

class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum2(self, candidates, target):
        candidates.sort()
        self.collection = []
        temp = []
        self.dfs(candidates, 0, target, 0, temp)
        return self.collection
    
    def dfs(self, candidates, now, target, start, temp):
        if now == target:
           self.collection.append(temp[:])
           return
        if now > target: 
           return
        l = len(candidates)
        i = start
        while i < l:
            count = 0
            while i+count<l-1 and candidates[i+count] == candidates[i+count+1]: 
              count += 1 
            temp.append(candidates[i])
            self.dfs(candidates, now+candidates[i], target, i+1, temp)
            temp.pop()
            i += count + 1
        return
       
if __name__ == '__main__':
   candidates = [10, 1, 2, 7, 6, 1, 5]
   candy = [2,2,2,1]
   can = [4,4,2,1,4,2,2,1,3]
   test = Solution()
   out = test.combinationSum2(candidates, 8)
   print out

  
