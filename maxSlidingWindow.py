# -*- coding: utf-8 -*-
# Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

# For example,
# Given nums = [1,3,-1,-3,5,3,6,7], and k = 3.

# Window position                Max
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7
# Therefore, return the max sliding window as [3,3,5,5,6,7].\

# Note: 
# You may assume k is always valid, ie: 1 ≤ k ≤ input array's size for non-empty array.


class Solution(object):
 
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if nums == []: return []
        
        localmax = (nums[0], 0) 
        for i in range(k):
            if nums[i] >= localmax[0]:
                localmax = (nums[i], i)
        out = [localmax[0]]
        
        j = k
        while j < len(nums):
            if j < localmax[1]+k:
                if nums[j] >= localmax[0]: localmax =  (nums[j], j)
            else: 
                localmax = (nums[j-k+1], j-k+1)
                for m in range(j-k+2, j+1):
                    if nums[m] >= localmax[0]: localmax = (nums[m], m)
            out.append(localmax[0])        
            j += 1
        return out