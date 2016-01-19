#Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

#Given num = 38, the process is like: 3 + 8 = 11, 1 + 1 = 2. Since 2 has only one digit, return it.

#Follow up:
#Could you do it without any loop/recursion in O(1) runtime?

class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        numstr = str(num)
        sumi = sum([int(i) for i in numstr])
        if sumi >= 10:
            sumi = self.addDigits(sumi)
        return sumi