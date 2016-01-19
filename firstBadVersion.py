# You are a product manager and currently leading a team to develop a new product. 
# Unfortunately, the latest version of your product fails the quality check. 
# Since each version is developed based on the previous version, all the versions after a bad version are also bad.

# Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

# You are given an API bool isBadVersion(version) which will return whether version is bad. Implement a function to find the first bad version. 
# You should minimize the number of calls to the API.

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if isBadVersion(n) == False: return
        if isBadVersion(1) == True: return 1
        return self.DFS(1, n)
        
    def DFS(self, start, end):
        if end == start + 1:
            return start if isBadVersion(start) == True else end
        mid = (start+end)/2
        if isBadVersion(mid) == True:
            return self.DFS(start, mid)
        else:
            return self.DFS(mid, end)