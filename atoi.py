# Implement atoi to convert a string to an integer.

class Solution:
    # @return an integer
    def atoi(self, s):
        if s == '': return 0           
        sign = 1  
        num = 0
        power = 10
        maxi = 2147483647
        mini = -2147483648
           
        for i in range(len(s)):
            if s[i] == ' ': continue
            break 

        if s[i] == '+' or s[i] == '-':
            if i == len(s) -1: return 0
            if s[i] == '-': sign = -1 
            s = s[i+1:]
        else: s = s[i:]
       
        for i in s:       
            if i.isdigit():
                num = num*power + (ord(i) - ord('0'))
            else: break
        
        num *= sign             
        if num > maxi: return maxi
        elif num < mini: return mini
        else: return num        
        
if __name__ == '__main__':
    test = Solution()
    out = test.atoi('    010')