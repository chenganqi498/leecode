# Given a collection of numbers, return all unique permutations.
# For example,
# [1,1,2] have the following unique permutations:
# [1,1,2], [1,2,1], and [2,1,1].

class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    
    # per(1) = 1
    # per(n) = per(n-1)*n    
    def permuteUnique(self, num):
        p0 = [[num[0]]] # permutations at step n-1
        for i in range(1, len(num)):
            p1 = []
            for item in p0:  
                j = 0    
                while j <= len(item):
                    if j < len(item) and item[j] == num[i]: 
                       j += 1
                       continue
                    new = item[0:j] + [num[i]] + item[j:]
                    if new not in p1: p1.append(new)
                    j += 1                                             
            p0 = p1
        return p0

if __name__ == '__main__':
    test = Solution()
    out = test.permuteUnique([1,1,2,2])
    print out
