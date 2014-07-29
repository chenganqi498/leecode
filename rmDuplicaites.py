# Remove duplicates from sorted array in place

class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if len(A) == 0:
            return
            
        sz = 1
        i = 0
        for i in range(len(A)-1):
            if A[i] != A[i+1]:
                A[sz] = A[i+1]
                sz += 1
        A = A[:sz]
        return  sz
                
if __name__ == '__main__':
    A = [1,2,3,4,5,6,6,7,7,8]
    out = Solution()
    print out.removeDuplicates(A)