#Related to question Excel Sheet Column Title
#Given a column title as appear in an Excel sheet, return its corresponding column number.
#For example:
#    A -> 1
#    B -> 2
#    C -> 3
#    ...
#    Z -> 26
#    AA -> 27
#    AB -> 28 

class Solution:
    # @param {string} s
    # @return {integer}
    def titleToNumber(self, s):
        dic = {'A':1, 'B':2,'C':3, 'D':4, 'E':5,'F':6, 'G':7, 'H':8, 'I':9, 'J':10, 'K':11,\
               'L':12, 'M':13, 'N':14, 'O':15, 'P':16, 'Q':17, 'R':18, 'S':19, 'T':20,\
               'U':21, 'V':22, 'W':23, 'X':24, 'Y':25, 'Z':26}
        out = 0
        ls = len(s)
        for i in range(ls-1, -1, -1):
            out += 26**(ls-i-1)*dic[s[i]]
        return out

if __name__ == '__main__':
    l = ['C','D','E','J','L','N','P','Q','R','S','T','U','V','AD','AE','AW','BD','BG','BN', 'BO',\
         'BP', 'BQ', 'BS']
    x = Solution()
    print map(lambda i:x.titleToNumber(i), l)
           