# Given an array of integers, find out whether there are two distinct indices i and j in the array 
# such that the difference between nums[i] and nums[j] is at most t and the difference between i and j is at most k.

class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        seq = sorted(range(len(nums)), key=nums.__getitem__)
        for i in range(len(nums)-1):
            counter = 1
            while i+counter < len(nums) and nums[seq[i+counter]]-nums[seq[i]] <= t:
                if abs(seq[i+counter]-seq[i]) <= k:
                    return True
                counter += 1

        return False