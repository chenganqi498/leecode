# Given two numbers represented as strings, 
# return multiplication of the numbers as a string.

# Note: The numbers can be arbitrarily large and are non-negative.

class Solution:
    # @param num1, a string
    # @param num2, a string
    # @return a string
    def multiply(self, num1, num2):
        n1 = int(num1) if num1.isdigit() else float(num1)
        n2 = int(num2) if num2.isdigit() else float(num2)
        return str(n1*n2)
    
if __name__ == '__main__':
    num1 = '45.4'
    num2 = '42.3'
    test = Solution()
    out = test.multiply(num1, num2)