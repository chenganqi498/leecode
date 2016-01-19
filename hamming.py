# -*- coding: utf-8 -*-
#Write a function that takes an unsigned integer and returns the number of ’1' bits it has 
#(also known as the Hamming weight).

#For example, the 32-bit integer ’11' has binary representation 
#00000000000000000000000000001011, so the function should return 3.

class Solution:
    # @param n, an integer
    # @return an integer
    def hammingWeight(self, n):
        count = []
        res = abs(n)
        while res > 0:
            count.append(res%2)
            res = res/2    
        return sum(count)    
            
        
if __name__ == '__main__':
    x = Solution()
    print x.hammingWeight(11)