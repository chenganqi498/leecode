# Given an index k, return the kth row of the Pascal's triangle.
# For example, given k = 3,
# Return [1,3,3,1].
# Note:
# Could you optimize your algorithm to use only O(k) extra space?

class Solution:
    # @return a list of lists of integers
    def getRow(self, rowIndex):
        prev = []
        for i in range(rowIndex+1):
            curr = [1]*(i+1)
            for j in range(1,i):
                curr[j] = prev[j-1]+prev[j]
            prev = curr
        return curr

if __name__ == '__main__':
   test = Solution()
   out = test.getRow(3)
   print out



