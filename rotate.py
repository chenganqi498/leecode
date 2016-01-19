#Rotate an array of n elements to the right by k steps.

#For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].

#Note:
#Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem. 

class Solution:
    # @param nums, a list of integer
    # @param k, num of steps
    # @return nothing, please modify the nums list in-place.
    def rotate(self, nums, k):
        k = k%len(nums)
        if k == 0: return 
        temp = nums[-k:]
        nums[k:] = nums[:len(nums)-k]
        nums[:k] = temp
        
if __name__ == '__main__':
    nums = range(1,8)
    print nums
    x = Solution()
    x.rotate(nums, 3)
    print nums