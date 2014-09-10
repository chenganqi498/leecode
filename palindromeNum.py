# Determine whether an integer is a palindrome. 
# Do this without extra space.

class Solution:
    # @return a boolean
    def isPalindrome(self, x):
        if x < 0: return False
        a, b = x, 0
        while a != 0:
          a, b = a/10, b*10 + a%10
        return b == x

if __name__ == '__main__':
   num = 0
   test = Solution()
   out = test.isPalindrome(num)
