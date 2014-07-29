def pow(x, n):
    x0 = x
    if n == 0:
      return 1
      
    if n == 1:
        return x
    
    i = 1
    while 2*i < n:
        x *= x
        i *= 2
        print x, i
        
    x *= pow(x0, n - i)
    
    return x

if __name__ == '__main__':
    print pow(2, 11)