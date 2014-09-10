# Given an array S of n integers, 
# are there elements a, b, c, and d in S such that a + b + c + d = target? 
# Find all unique quadruplets in the array which gives the sum of target.
#    For example, given array S = {1 0 -1 0 -2 2}, and target = 0.
#    A solution set is:
#    (-1,  0, 0, 1)
#    (-2, -1, 1, 2)
#    (-2,  0, 0, 2)

# exceed time limit on large data set
class Solution:
    # @return a list of lists of length 4, [[val1,val2,val3,val4]]
    def fourSum(self, num, target):
        num.sort()
        l = len(num)
        out = set()
        
        for i in range(l-3):
            if i > 0 and num[i] == num[i-1]: continue
            for j in range(i+1, l-2):
                if j > 0 and num[j] == num[j-1]: continue
                m, n = 1, 1 
                while j+m < l-n:
                   sumi = (num[i], num[j], num[j+m], num[l-n])
                   if sum(sumi) == target:
                      out.add(sumi)
                      m += 1
                      n += 1
                   elif sum(sumi) > target:
                      n += 1
                   else: m += 1
        return list(out)

if __name__ == '__main__':
   s = [1, 0, -1, 0, -2, 2]
   test = Solution()
   out = test.fourSum(s, 0)
   print out          
          

