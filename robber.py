#House Robber Total Accepted: 8708 Total Submissions: 30753
#You are a professional robber planning to rob houses along a street. 
#Each house has a certain amount of money stashed, 
#the only constraint stopping you from robbing each of them is that 
#adjacent houses have security system connected and it will automatically contact the police 
#if two adjacent houses were broken into on the same night.

#Given a list of non-negative integers representing the amount of money of each house, 
#determine the maximum amount of money you can rob tonight without alerting the police.

class Solution:
    # @param num, a list of integer
    # @return an integer
    def rob(self, num):
        sumi1, sumi2= 0, 0
        for i in range(len(num)):
           temp = sumi2
           sumi2 = sumi1 + num[i]
           sumi1 = max(temp, sumi1)
        return max(sumi1, sumi2)
           
if __name__ == '__main__':
   num = [2,1,1,2,2]
   x = Solution() 
   print x.rob(num)