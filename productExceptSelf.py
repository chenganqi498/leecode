#Given an array of n integers where n > 1, nums, return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

#Solve it without division and in O(n).

#For example, given [1,2,3,4], return [24,12,8,6].

#Follow up:
#Could you solve it with constant space complexity? (Note: The output array does not count as extra space for the purpose of space complexity analysis.)

class Solution:
    # @param {integer[]} nums
    # @return {integer[]}
    def productExceptSelf(self, nums):
        l = len(nums)
        head, tail = 1, 1
        heads, tails = [1],[1] 
        out = []

        for i in range(l-1):
            head *= nums[i]
            tail *= nums[l-1-i]
            heads.append(head)
            tails.append(tail)
    
        for i in range(l):
            out.append(heads[i]*tails[l-1-i])
        
        return out