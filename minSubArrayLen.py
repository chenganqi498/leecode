# -*- coding: utf-8 -*-
# Given an array of n positive integers and a positive integer s, 
# find the minimal length of a subarray of which the sum ≥ s. If there isn't one, return 0 instead.

# For example, given the array [2,3,1,2,4,3] and s = 7,
# the subarray [4,3] has the minimal length under the problem constraint.

class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if sum(nums) < s: return 0
        l = len(nums)
        bucket = []
        for i in range(len(nums)):
            bucket.append(nums[i])
            while sum(bucket) >= s:
                l = min(l, len(bucket))
                bucket.pop(0)
        return l    
                
        