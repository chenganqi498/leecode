# Given n non-negative integers representing the histogram's bar height 
# where the width of each bar is 1, 
# find the area of largest rectangle in the histogram.
# For example,
# Given height = [2,1,5,6,2,3],
# return 10.

class Solution:
    # @param height, a list of integer
    # @return an integer
    def largestRectangleArea(self, height):
        height.append(0)
        i, l = 0, len(height)
        maxarea = 0
        index = []
        while i < l:
            if index == [] or height[i] >= height[index[-1]]:
               index.append(i)
               i += 1
            else: 
               curr = index.pop()
               area = height[curr]*i if index == [] else height[curr]*(i-index[-1]-1)
               maxarea = max(maxarea, area)
        return maxarea

if __name__ == '__main__':
   height = [4,2,0,3,2,5]
   test = Solution()
   out = test.largestRectangleArea(height)
   print out
