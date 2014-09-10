# The count-and-say sequence is the sequence of integers beginning as follows:
# 1, 11, 21, 1211, 111221, ...

# 1 is read off as "one 1" or 11.
# 11 is read off as "two 1s" or 21.
# 21 is read off as "one 2, then one 1" or 1211.
# Given an integer n, generate the nth sequence.

# Note: The sequence of integers will be represented as a string.

class Solution:
    # @return a string
    def countAndSay(self, n):
        now = '1'
        for k in range(1, n):
            out = ''
            i = 0
            while i < len(now):
               say = now[i]
               count = 1
               while i < len(now) -1 and now[i] == now[i+1]:
                  count += 1
                  i += 1
               out += str(count)+say
               i += 1
            now = out

        return now

if __name__ == '__main__':
   n = 5
   test = Solution()
   out = test.countAndSay(n)
