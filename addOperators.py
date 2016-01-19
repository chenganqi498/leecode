# Given a string that contains only digits 0-9 and a target value, 
# return all possibilities to add binary operators (not unary) +, -, or * between the digits 
# so they evaluate to the target value.

# Examples: 
# "123", 6 -> ["1+2+3", "1*2*3"] 
# "232", 8 -> ["2*3+2", "2+3*2"]
# "105", 5 -> ["1*0+5","10-5"]
# "00", 0 -> ["0+0", "0-0", "0*0"]
# "3456237490", 9191 -> []

class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        self.nums = [int(i) for i in num]
        self.target = target
        self.l = len(self.nums)
        self.collect = []
        self.DFS(self.nums[0], [], 0)
        
        return self.collect
        
    def DFS(self, curr, ops, i):
        if i >= self.l-1:
            if curr == self.target:
               return ops
            return
        nt = self.nums[i+1]
        multiply = curr*nt
        plus = curr+nt
        minus = curr-nt
        multiply = self.DFS(curr*nt, ops+['*'], i+1)
        plus = self.DFS(curr+nt, ops+['+'], i+1)
        minus = self.DFS(curr-nt, ops+['-'], i+1)
        for i in [multiply, plus, minus]:
            if i != None:
                self.collect.append(i)
