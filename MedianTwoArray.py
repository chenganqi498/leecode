# median of two sorted array

class Solution:
    
    def findMedian(self, A, B):
        la = len(A)
        lb = len(B)
        
        if (la + lb)%2 == 0:
            return (self.findK(A,B,(la+lb)/2) +\
                    self.findK(A,B,(la+lb)/2+1))/2.0
        else:
            return self.findK(A,B,(la+lb+1)/2)
           
    def findK(self, A, B, K):           
        la, lb = len(A), len(B)        
        ta = min(la, K/2)
        tb = min(lb, K - ta)  
        
        if la == 0:
            return B[K-1]
            
        if lb == 0:
            return A[K-1]
            
        if K == 1:
            return min(A[0], B[0])
        
        if A[ta - 1] < B[tb - 1]:          
            return self.findK(A[ta:], B, K - ta)
               
        elif A[ta-1] > B[tb-1]:
            return self.findK(A, B[tb:], K - tb)
            
        else: 
            return A[ta - 1]          
      
if __name__ == '__main__':
    A = [0]
    B = [1,2]

    out = Solution()
    print out.findMedian(A,B)