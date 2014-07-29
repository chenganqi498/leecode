def maxsub(lt):
    maxi, sumi = lt[0], lt[0]
    for i in lt[1:]:
        if sumi <= 0:
            sumi = i
        else:
            sumi += i
        maxi = max(maxi, sumi)
    
    return maxi

if __name__ == '__main__':
    lt = [-2]
    print maxsub(lt)
    