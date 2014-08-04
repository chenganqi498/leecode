# Given a digit string, 
# return all possible letter combinations that the number could represent.

class Solution:
    # @return a list of strings, [s1, s2]
    def letterCombinations(self, digits):
        mapper = {'0':' ', '1':'', '2':'abc', '3':'def', '4':'ghi', '5':'jkl',\
                   '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}                
        comb = ['']
        for i in digits:
            temp = []
            for j in comb:
                for k in mapper[i]:
                  temp.append(j + k)
            if temp != []: comb = temp
            
        return comb

if __name__ == '__main__':
    test = Solution()
    out = test.letterCombinations('23')
                
            
                
                