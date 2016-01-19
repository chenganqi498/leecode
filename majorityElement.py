# -*- coding: utf-8 -*-
#Given an array of size n, find the majority element. 
#The majority element is the element that appears more than ⌊ n/2 ⌋ times.

#You may assume that the array is non-empty and the majority element always exist in the array.

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def majorityElement(self, nums):
        dic = {}
        rec = 0
        out = None
        for i in nums:
            if i not in dic:
                dic[i] = 1
            else: dic[i] += 1
            if dic[i] > rec: out = i
            rec = max(rec, dic[i])
        return out
        
if __name__ == '__main__':
    nums = [1,2,1,2,4,2]
    x = Solution()
    print x.majorityElement(nums)
    
    