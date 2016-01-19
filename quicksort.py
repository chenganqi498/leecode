# quick sort, follow:
# http://www.youtube.com/watch?v=aQiWF4E8flQ
# which is super clear and easy!

def partition(lt, start, end):  
    pivot = lt[end]
    wall = start # wall to the left of the start element
    
    for current in range(start, end):
        if lt[current] < pivot:
            # exchange current element with the element right next to the wall
            lt[current], lt[wall] = lt[wall], lt[current]
            # move the wall to the right of the element smaller the pivot
            wall += 1
    # put the pivot to the position of the wall
    lt[wall], lt[end] = lt[end], lt[wall]
    return wall

def quicksort(lt, start, end):
    if start < end:
        wall = partition(lt, start, end)
        quicksort(lt, start, wall-1)
        quicksort(lt, wall+1, end)