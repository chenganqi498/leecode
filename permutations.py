# Given a collection of numbers, return all possible permutations.
# For example,
# [1,2,3] have the following permutations:
# [1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], and [3,2,1].

class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    
    # per(1) = 1
    # per(n) = per(n-1)*n    
    def permute(self, num):
        p0 = [[num[0]]] # permutations at step n-1
        
        
        for i in range(1, len(num)):
            for item in p0:  
                j = 0    
                p1 = [] #permutations at step n
                while j <= len(item):
                    # insert num[i] before item[j]
                    p1.append(item[0:j] + [num[i]] + item[j:])
                    # avoid duplicates
                    if j != len(item) and item[j] == num[i]: j += 2
                    else: j += 1                                             
            p0 = p1
            
            
        return p0

if __name__ == '__main__':
    test = Solution()
    out = test.permute([1,1,1])