# A message containing letters from A-Z is being encoded to numbers using the following mapping:
# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26

# Given an encoded message containing digits, 
# determine the total number of ways to decode it.

# For example,
# Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).
# The number of ways decoding "12" is 2.

class Solution:
    # @param s, a string
    # @return an integer
   
    def numDecodings(self, s):
#-----------------initialization----------------
        if s == '' or s[0] == '0': return 0          
        l = len(s)
        ways0, ways1 = 1, 1
        digit = lambda x: ord(x) - ord('0')
        
        if l == 1: return ways0
    
        num = digit(s[0])*10 + digit(s[1])
        if num > 10 and num < 27 and num != 20: 
            ways1 = 2
        elif num > 27 and num%10 == 0:
            ways1 = 0
#-----------------dp-----------------------------           
        for i in range(2, l):
            num = digit(s[i-1])*10 + digit(s[i])
            if num > 10 and num < 27 and num != 20:
               temp =  ways0 + ways1        
            elif num == 10 or num == 20:
               temp = ways0
            elif num%10 != 0:
               temp = ways1     
            else: return 0     
            ways0, ways1 = ways1, temp
            
        return ways1
 
if __name__ == '__main__':
    test = Solution()
    num = "47575625458446174945557745813412115112968167865867877552577411785\
           99337186486723247528324612117156948"
    out = test.numDecodings(num)
    