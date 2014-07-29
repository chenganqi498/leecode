# Given an array and a value, 
# remove all instances of that value in place and return the new length.
# The order of elements can be changed. 
# It doesn't matter what you leave beyond the new length.

def removeElement_v1(A, elem):
    while True:
        try:
            A.remove(elem)
        except ValueError:
          return len(A)

def removeElement_v2(A, elem):
        j = 0 
        for i in A:
          if i != elem:
            A[j] = i
            j += 1
            
        return j
        
if __name__ == '__main__':
    A = [1,3,5,7,9,2,4,6,8,10,1]
    print removeElement_v1(A, 11)