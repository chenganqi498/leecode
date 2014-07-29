def merge(A, m, B, n):
    A += B
    
    for k in range(m+n-1, -1, -1):
        # make sure A[-1] or B[-1] does not appear
        if m == 0 or (n > 0 and A[m-1] < B[n-1]):
            A[k] = B[n-1]
            n -= 1
        else:
            A[k] = A[m-1]
            m -= 1
                 
    return A
            
if __name__ == '__main__':
    A = [1,3,5,7,9]
    B = [0,2,4]
    print merge(A,5,B,3)