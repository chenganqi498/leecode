# Given an unsorted array of integers, 
# find the length of the longest consecutive elements sequence.

# For example,
# Given [100, 4, 200, 1, 3, 2],
# The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.

# Your algorithm should run in O(n) complexity.

class Solution:
    # @param num, a list of integer
    # @return an integer   
    def longestConsecutive(self, num):
        if num == []: return 0
        hashmap = {}
        for i in range(len(num)):hashmap[num[i]] = i
        maxlen = 1
    
        for i in range(len(num)):        
           if num[i] not in hashmap: continue  
           length = 1
           del hashmap[num[i]]
           
           for direction in [-1, 1]:
               elem = num[i]
               while elem + direction in hashmap: 
                   length += 1   
                   del hashmap[elem + direction]
                   elem += direction
                         
           maxlen = max(maxlen, length)
           
        return maxlen
              
    def findNext(self, elem, hashmap, direction):    
        if elem + direction in hashmap:
            del hashmap[elem + direction]
            self.length += 1
        return hashmap       

if __name__ == '__main__':
    num = [1, 2, 0 ,1]
    test = Solution()
    out = test.longestConsecutive(num)
    