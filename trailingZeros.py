#Given an integer n, return the number of trailing zeroes in n!.

#Note: Your solution should be in logarithmic time complexity.

class Solution:
    # @param {integer} n
    # @return {integer}
    def trailingZeroes(self, n):
        res, count = n, 0 
        while res > 0:
              res = res/5
              count += res
        return count

if __name__ == '__main__':
    x = Solution()
    print x.trailingZeroes(30)
        