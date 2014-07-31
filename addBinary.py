# Given two binary strings, 
# return their sum (also a binary string).

# For example,
# a = "11", b = "1"
# Return "100".

class Solution:
    # @param a, a string
    # @param b, a string
    # @return a string
    def addBinary(self, a, b):
        if a == '' and b == '': return ''
        c = ''
        add = '0'
      
        while a != '' or b != '':       
            if (a == '' or a[-1] == '0') and (b == '' or b[-1] == '0'):
               c += add  
               add = '0'
            elif a != '' and a[-1] == '1' and b != '' and b[-1] == '1':
                  c += add
                  add = '1'
            elif add == '1':
                  c += '0'
            else:
                  c += '1'          
            a = a[:-1] if a != '' else ''
            b = b[:-1] if b != '' else ''    
                       
        c = c + add if add == '1' else c                 
        return c[::-1]
    
if __name__ == '__main__':
    test = Solution()
    a = '1010'
    b = '1011'
    out = test.addBinary(a,b)
    
        