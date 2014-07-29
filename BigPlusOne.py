# big number plus one

class Solution:
    # @param digits, a list of integer digits
    # @return a list of integer digits
    def plusOne(self, digits):
        l = len(digits)    
        digits[l-1] += 1
        
        for i in range(l-1, -1, -1):
            if digits[i] == 10:
                if i == 0:
                    digits = [1] + [0]*l
                else:
                    digits[i] = 0
                    digits[i-1] += 1
            else: 
                break
        
        return digits 
            
if __name__ == '__main__':
    digits = [1,0,6,5,8,3,9,9]
    out = Solution().plusOne(digits)
    