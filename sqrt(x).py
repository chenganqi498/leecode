# Implement int sqrt(int x).
# Compute and return the square root of x.

class Solution:
    # @param x, an integer
    # @return an integer
    
    # Newton's method
    # y = sqrt(x)
    # f(y) = y^2 - x
    # f'(y) = 2y
    # f(y0) = (y0-y1)*f'(y0) => y1 = y0 - f(y0)/f'(y0)
    # y1 = y0 - (y0^2 - x)/(2y0) 
    def sqrt(self, x):
        y0 = 0 
        y1 = 1
            
        while int(y0) != int(y1):
           y0 = y1
           y1 = y0 - (y0**2 - x)/(2.0*y0)   
        return int(y1)
        
if __name__ == '__main__':
    test = Solution()
    out = test.sqrt(1)