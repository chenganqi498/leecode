# Climbing Stairs
# Recursion f(n) = f(n-1) + f(n-2)
def climbStairs(n):
   if n == 1: return 1
   if n == 2: return 2
   
   fn = 0
   fn1 = 2
   fn2 = 1
   
   for i in range(2, n):
       fn = fn1 + fn2
       fn2 = fn1
       fn1 = fn
   
   return fn
   
if __name__ == '__main__':
    print climbStairs(10)