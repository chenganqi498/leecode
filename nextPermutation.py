# Implement next permutation, 
# which rearranges numbers into the lexicographically next greater permutation of numbers.

# If such arrangement is not possible, 
# it must rearrange it as the lowest possible order (ie, sorted in ascending order).

# The replacement must be in-place, do not allocate extra memory.

# Here are some examples. 
# Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
# 1,2,3 -> 1,3,2
# 3,2,1 -> 1,2,3
# 1,1,5 -> 1,5,1

# Follow instructions online, don't quite understand
class Solution:
    # @param num, a list of integer
    # @return a list of integer
    def nextPermutation(self, num):
        if num == []: return []
        l = len(num)
        exist1, exist2 = False, False
        for i in range(l-1, 0, -1):
            if num[i] > num[i-1]: 
               exist1 = True
               break        
        if exist1:
            for j in range(l-1, i-1, -1):
                if num[j] > num[i-1]: 
                   exist2 = True
                   break
        if exist1 and exist2:
           num[i-1], num[j] = num[j], num[i-1]
           for k in range((l-i)/2):
               num[i+k], num[l-1-k] = num[l-1-k], num[i+k]
        else:
           for k in range(l/2):
               num[k], num[l-1-k] = num[l-1-k], num[k]
        return num

if __name__ == '__main__':
   num = [3,2,1]
   test = Solution()
   out = test.nextPermutation(num)
   print out
