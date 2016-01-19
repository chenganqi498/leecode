#Given an array of integers and an integer k, 
#find out whether there there are two distinct indices i and j in the array such that nums[i] = nums[j] 
#and the difference between i and j is at most k. 

class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {boolean}
    def containsDuplicate(self, nums, k):
        had = {}
        for i in range(len(nums)):
            if nums[i] not in had: had[nums[i]]=i
            elif i - had[nums[i]] <= k: return True
            else: had[nums[i]] = i
        return False