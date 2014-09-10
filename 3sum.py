# Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? 
# Find all unique triplets in the array which gives the sum of zero.

#    For example, given array S = {-1 0 1 2 -1 -4},
#    A solution set is:
#    (-1, 0, 1)
#    (-1, -1, 2)

class Solution:
    # @return a list of lists of length 3, [[val1,val2,val3]]
    def threeSum(self, num):
        num.sort()
        l = len(num)
        out = []
    
        for i in range(l-2):
          j, k = 1, 1
          while i+j < l-k:
             sumi = [num[i], num[i+j], num[l-k]]
             if sum(sumi) == 0:
                if sumi not in out:
                   out.append(sumi)
                j += 1
                k += 1
             elif sum(sumi) > 0:
                k += 1
             else:  
                j += 1

        return out
   
if __name__ == '__main__':
   num = [-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]
   test = Solution()
   out = test.threeSum(num)
