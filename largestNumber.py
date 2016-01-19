# Given a list of non negative integers, arrange them such that they form the largest number.

# For example, given [3, 30, 34, 5, 9], the largest formed number is 9534330.

# Note: The result may be very large, so you need to return a string instead of an integer.

class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        nums = map(lambda x: ','.join(x).split(','), nums)
        sortbylen = {}
        for i in nums:
            if len(i) in sortbylen:
                sortbylen[len(i)].append(i)
            else: sortbylen[len(i)] = [i]
            
        for key in sortbylen.keys():
            sortbylen[key].sort()
        
        
        
            
        
        
        
        
        
        