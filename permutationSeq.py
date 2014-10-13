# The set [1,2,3,...,n] contains a total of n! unique permutations.

# By listing and labeling all of the permutations in order,
# We get the following sequence (ie, for n = 3):

# "123"
# "132"
# "213"
# "231"
# "312"
# "321"
# Given n and k, return the kth permutation sequence.

# Note: Given n will be between 1 and 9 inclusive.

class Solution:
    # @return a string
    def getPermutation(self, n, k):
        if n == 1 and k == 1: return '1'
        out = ''
        tol = 1
        for i in range(1, n): tol *= i
        num = range(1, n+1)
      
        for j in range(n-1, 0, -1):
            factor = k/tol
            res = k%tol
            if res == 0:
               out += str(num.pop(factor-1))
               for i in num[::-1]: out += str(i)
               return out
            out += str(num[factor])
            num.pop(factor)
            if num == []: return out
            tol /= j
            k = res

if __name__ == '__main__':
   test = Solution()
   out = test.getPermutation(3,1)
   print out
