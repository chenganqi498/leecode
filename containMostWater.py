# Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). 
# n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). 
# Find two lines, which together with x-axis forms a container, 
# such that the container contains the most water.

class Solution:
    # @return an integer
    def maxArea(self, height):
        maxArea = 0
        left, right = 0, len(height)-1
        while left < right:
           area = min(height[left], height[right])*(right-left)
           if height[left] < height[right]: left += 1
           else: right -= 1
           maxArea = max(maxArea, area)
        return maxArea
        
