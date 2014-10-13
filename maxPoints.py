# Given n points on a 2D plane, 
# find the maximum number of points that lie on the same straight line.

# Definition for a point
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

class Solution:
    # @param points, a list of Points
    # @return an integer
    def maxPoints(self, points):
        if len(points) <=2: return len(points)
        coeffs = {}
        tol = 2
        for end in range(len(points)):
            for start in range(end):
                new = self.line(points[start], points[end])
                if new in coeffs:
                   if start not in coeffs[new]: coeffs[new].append(start)
                   if end not in coeffs[new]: coeffs[new].append(end)
                else:  coeffs[new] = [start, end]
                tol = max(tol, len(coeffs[new]))
        return tol
        
    def line(self, pt1, pt2):
        a = float('inf') if pt1.x == pt2.x else\
                           1.0*(pt1.y-pt2.y)/(pt1.x-pt2.x)
        b = pt1.y - a*pt1.x
        return (a,b)

if __name__ == '__main__':
   
   points = [Point(1,1), Point(1,1), Point(0,0)]
   test = Solution()
   out = test.maxPoints(points)
   print out
