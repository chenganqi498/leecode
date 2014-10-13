# Given two words (start and end), and a dictionary, 
# find the length of shortest transformation sequence from start to end, 
# such that:
# 1.Only one letter can be changed at a time
# 2.Each intermediate word must exist in the dictionary

# For example,
# Given:
# start = "hit"
# end = "cog"
# dict = ["hot","dot","dog","lot","log"]
# As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
# return its length 5.

# Note:
# Return 0 if there is no such transformation sequence.
# All words have the same length.
# All words contain only lowercase alphabetic characters.

# @param start, a string
# @param end, a string
# @param d, a set of string
# @return an integer

# time limit exceed  
class Solution:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return an integer
    def ladderLength(self, start, end, d):
        curr = [start]
        count = 2
        while curr != []:
           temp = []
           for i in curr:
               if self.distance(i, end): return count
               for j in d:
                   if j not in temp and self.distance(i,j):
                      temp.append(j)
           for k in temp: d.remove(k)    
           curr = temp
           count += 1
        return 0

    def distance(self, s1, s2):
        count = 0
        for i in range(len(s1)):
            if s1[i] != s2[i]: count += 1
            if count > 1: return False
        return True

if __name__ == '__main__':
   start = "red"
   end = "tax"
   dict = set(["ted","tex","red","tax","tad","den","rex","pee"])

   test = Solution()
   out =  test.ladderLength(start, end, dict)
   print out
