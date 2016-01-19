# Given a sorted integer array without duplicates, return the summary of its ranges.
# For example, given [0,1,2,4,5,7], return ["0->2","4->5","7"].

class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        out = []
        if len(nums) == 0: return []
        start, end = nums[0], nums[0]
        i = 1
        while i < len(nums):
            if nums[i] == nums[i-1]+1:
                end = nums[i]
            else:
                if start == end:
                   out.append(str(start))
                else:
                   out.append(str(start)+'->'+str(end))
                start, end = nums[i], nums[i]
            i += 1
        
        if start == end:
           out.append(str(start))
        else:
           out.append(str(start)+'->'+str(end))
        return out
        

