# mergesort

# the two sorted sublists to be merged are:
# lt[left:mid] and lt[mid, right]

def merge(lt, left, mid, right):
    i, j = left, mid
    lt3 = [0] * len(lt) #temporarily store sorted sublist
    
    for k in range(left, right): # lt3[left:right] will store sorted results
        # if scanning lt[left:mid] hasn't over, 
        # and the element in lt[left:mid] is smaller than that in lt[mid:right], 
        # or lt[mid:right] has been scanned over
        # change lt[k] to the element in lt[left:mid]
        if  i < mid and (j >= right or lt[i] < lt[j]):
            lt3[k] = lt[i]
            i += 1
        # else (i.e. lt[left:mid] has been scanned over,
        # or element in lt3[left:mid] is larger than lt3[mid:right]
        else:
            lt3[k] = lt[j]
            j += 1 
            
    # overwrite the sublist lt[left:right] to the sorted one           
    lt[left:right] = lt3[left:right]
     
def mergesort(lt):
    # started with sublist of width 1
    width = 1
    
    # max of with is len(lt)
    while width <= len(lt):
        # merge sublists lt[i:i+width] and lt[i+width:i+2*width]
        for i in range(0, len(lt), 2*width):
            mid = min(i+width, len(lt))
            right = min(i+2*width,len(lt))
            if mid < right:
                merge(lt, i, mid ,right)
        # double size of the sublists to be merged in the next step
        width *= 2
  
        