# 3 sum
def threeSum(num):
    num.sort()
    l = len(num)
    out = []
    
    for i in range(l-2):
        j, k = 1, 1
        if i > 0 and num[i] == num[i-1]:
           continue
        while i+j < l-k:
           if num[i] + num[i+j] + num[l-k] == 0:
             out.append([num[i], num[i+j], num[l-k]])
             j += 1
             k += 1
           elif num[i] + num[i+j] + num[l-k] > 0:
               k += 1
           else:  
               j += 1
           
    return out
    
A = [0, 1, -1, 2, 3, -2, 4, 2]
print threeSum(A)