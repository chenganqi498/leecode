#Reverse bits of a given 32 bits unsigned integer.

#For example, given input 43261596 (represented in binary as 00000010100101000001111010011100), 
#return 964176192 (represented in binary as 00111001011110000010100101000000).

#Follow up:
#If this function is called many times, how would you optimize it? 

class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        count = []
        res = abs(n)
        new = 0
        while res > 0:
            count.append(res%2)
            res = res/2  
        count = count+[0]*(32-len(count))
        for i in range(32):
            if count[i] == 1: new += 2**(31-i)  
        return new

if __name__ == '__main__':
    x = Solution()
    print x.reverseBits(43261596)            