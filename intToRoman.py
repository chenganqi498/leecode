# Given an integer, convert it to a roman numeral.
# Input is guaranteed to be within the range from 1 to 3999.

class Solution:
    # @return a string
    def intToRoman(self, num):
        out = ''
        roman = 'MDCLXVI'
        inti =   [1000, 500, 100, 50, 10, 5, 1]
        
        i = 0
        while num > 0:
            print num
            fac = num // inti[i]
            res = num - fac*inti[i]
            if res != 0 and res//inti[i+1] == 4:
                if fac == 1:
                   out += roman[i+1] + roman[i-1]
                elif fac == 0:
                    out += roman[i+1] + roman[i]
                num = res - 4*inti[i+1]
                i += 2
            else:
                out += roman[i]*fac
                num = res
                i += 1
                
        return out

if __name__ == '__main__':
    test = Solution()
    num = 1040
    out = test.intToRoman(44)
        
            