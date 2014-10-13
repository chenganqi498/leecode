# The gray code is a binary numeral system 
# where two successive values differ in only one bit.

# Given a non-negative integer n representing the total number of bits in the code, 
# print the sequence of gray code. A gray code sequence must begin with 0.

# For example, given n = 2, return [0,1,3,2]. Its gray code sequence is:
# 00 - 0
# 01 - 1
# 11 - 3
# 10 - 2

# DP, hahahahaha
class Solution:
    # @return a list of integers
    def grayCode(self, n):
        if n == 0: return [0]
        bins = [[0],[1]]
        for i in range(1, n):
            temp = []
            for j in range(len(bins)):
                temp.append([0]+bins[j])
            for j in range(len(bins)-1, -1, -1):
                temp.append([1]+bins[j])
            bins = temp

        out = []
        for num in bins: out.append(self.binaryToDecimal(num))
        return out
         
    def binaryToDecimal(self, binary):
        num = 0
        l = len(binary)
        for i in range(l):
            num += 2**i * binary[l-1-i]
        return num

if __name__ == '__main__':
   test = Solution()
   out =  test.grayCode(2)
   print out


