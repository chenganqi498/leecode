#Write a program to find the n-th ugly number.

#Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. For example, 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.

#Note that 1 is typically treated as an ugly number.

#This soluiton exceed time limit
class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        uglys = [1]
        count = 1
        while count < n:
            new1 = self.findMin(uglys, 2)
            new2 = self.findMin(uglys, 3)
            new3 = self.findMin(uglys, 5)
            uglys.append(min(new1, new2, new3))
            count += 1
        return uglys[-1]
        
    def findMin(self, uglys, factor):
        for i in uglys:
            if i*factor > uglys[-1]:
                return i*factor
        

#Solution from Internet, very smart!
class Solution1:
    # @param {integer} n
    # @return {integer}
    def nthUglyNumber(self, n):
        q = [1]
        i2 = i3 = i5 = 0
        while len(q) < n:
            m2, m3, m5 = q[i2] * 2, q[i3] * 3, q[i5] * 5
            m = min(m2, m3, m5)
            if m == m2:
                i2 += 1
            if m == m3:
                i3 += 1
            if m == m5:
                i5 += 1
            q += m,
        return q[-1]