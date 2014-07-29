# Reverse digits of an integer.

# Example1: x = 123, return 321
# Example2: x = -123, return -321
def reverse(x):
    digit = len(str(abs(x)))
    if digit == 1:
        return x
    new = 0
    xabs = abs(x)
    sign = xabs/x
    
    
    for d in range(digit-1, -1, -1):
        new += xabs//(10**d) * 10**(digit-1-d)
        xabs =  xabs%(10**d)
    
    return sign*new
    
if __name__ == '__main__':
    x = 0
    out = reverse(x)



