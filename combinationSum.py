# -*- coding: utf-8 -*-
# Given a set of candidate numbers (C) and a target number (T), 
# find all unique combinations in C where the candidate numbers sums to T.

# The same repeated number may be chosen from C unlimited number of times.

# Note:
# All numbers (including target) will be positive integers.
# Elements in a combination (a1, a2, … , ak) must be in non-descending order.
# The solution set must not contain duplicate combinations.
# For example, given candidate set 2,3,6,7 and target 7, 
# A solution set is: [7] [2, 2, 3] 

class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum(self, candidates, target):
        candidates.sort()
        self.collection = []
        temp = []
        self.dfs(candidates, target, 0, 0, temp)      
        return self.collection
    
    def dfs(self, candidates, target, now, start, temp):
        if now == target: 
            # Attention: do NOT directly append temp, it will change!
            self.collection.append(temp[:]) 
            return
        if now > target: return
            
        for i in range(start, len(candidates)):    
               temp.append(candidates[i])
               self.dfs(candidates, target, now + candidates[i], i, temp)
               temp.pop() # hmmmm... smart!
      
  
if __name__ == '__main__':
    cand = [2,3,6,7]
    tar = 7
    test = Solution()
    out = test.combinationSum([2,3,5], 8)     