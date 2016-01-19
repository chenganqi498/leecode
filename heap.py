# Heap algorithm

class Solution():
 
    def heap(self, N, array):
        if N == 1:
            return array
        if N > len(array):
            return 'exceed array size'        
        
        for i in range(N):
            self.heap(N-1, array)
            if i < N-1: 
              array[0 if N%2 == 1 else i], array[N-1] =\
              array[N-1], array[0 if N%2 == 1 else i]
            
              print array
            
if __name__ == '__main__':
    A = [1,2,3,4,5,6,7,8,9]
    solution = Solution()
    solution.heap(3, A)