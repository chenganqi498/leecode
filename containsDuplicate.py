#Given an array of integers, find if the array contains any duplicates. 
#Your function should return true if any value appears at least twice in the array, 
#and it should return false if every element is distinct. 

class Solution:
    # @param {integer[]} nums
    # @return {boolean}
    def containsDuplicate(self, nums):
        had = {}
        for i in range(len(nums)):
            if nums[i] not in had: had[nums[i]]=i
            else: return True
        return False