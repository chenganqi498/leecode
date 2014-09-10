# Divide two integers without using multiplication, division and mod operator.

class Solution:
    # @return an integer
    def divide(self, dividend, divisor):
        dividend_sign = 1 if dividend > 0 else -1
        divisor_sign = 1 if divisor > 0 else -1
        dividend_abs = abs(dividend)
        divisor_abs = abs(divisor)
    
        factor = self.binarySearch(dividend_abs, divisor_abs) 
        return factor if dividend_sign == divisor_sign else 0-factor
        
    def binarySearch(self, dividend, divisor):   
        if divisor > dividend: return 0    
        tol = divisor
        factor = 1
        while tol < dividend - tol:
            tol += tol
            factor += factor
            
        overhead = dividend - tol
        factor += self.binarySearch(overhead, divisor)       
        return factor
    
if __name__ == '__main__':
    test = Solution()
    out = test.divide(0, 3)