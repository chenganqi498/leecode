# Given an array S of n integers, 
# find three integers in S such that the sum is closest to a given number, target. 
# Return the sum of the three integers. 
# You may assume that each input would have exactly one solution.

class Solution:
    # @return an integer
    def threeSumClosest(self, num, target):
        if num == []: return
        num.sort()
        lnum = len(num)
        minres = float('inf')
        out = None

        for i in range(lnum):
            res = target - num[i]
            left, right = i+1, lnum-1
            while left < right:
               res2 = res - num[left] - num[right] 
               if res2 > 0: left += 1
               if res2 == 0: return target
               if res2 < 0: right -= 1
               if abs(res2) < abs(minres):
                  minres = res2
                  out = target - res2               
        return out

if __name__ == '__main__':
   test = Solution()
   out = test.threeSumClosest([0,0,0],1)
   print out

