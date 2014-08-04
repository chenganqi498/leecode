# Given a string containing only digits, 
# restore it by returning all possible valid IP address combinations.

# For example:
# Given "25525511135",

# return ["255.255.11.135", "255.255.111.35"]. (Order does not matter)

class Solution:
    # @param s, a string
    # @return a list of strings
    def restoreIpAddresses(self, s):
        self.ans = []
        temp = ''
        self.dfs(s, temp)
        return self.ans
    
    def dfs(self, s, temp):      
        sep = ''
        if temp != '': sep = temp[:-1].split('.')
        if len(sep) > 4: return
        for x in sep: 
            if int(x) > 255: return
        if s == '':
            if len(sep) == 4: self.ans.append(temp[:-1])
            return
        
        temp += s[0] +'.'
        self.dfs(s[1:], temp)
        temp = temp[:-2]
        if len(s) > 1 and s[0] != '0':
            temp += s[:2] + '.'
            self.dfs(s[2:], temp)
            temp = temp[:-3]
        if len(s) > 2 and s[0] != '0':
            temp += s[:3] + '.'
            self.dfs(s[3:], temp)
            temp = temp[:-4]
            
if __name__ == '__main__':
    s = '25525511135'
    test = Solution()
    out = test.restoreIpAddresses("010010")