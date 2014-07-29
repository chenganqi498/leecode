# Valid Parentheses

class Solution:
    # @return a boolean
    def isValid(self, s):    
        pair = {'(':')', '[':']', '{':'}'}
        
        stk = []
        for c in s:
            # if c is left side, apptend to stk
            if pair.get(c) != None:
               stk.append(c)

            elif len(stk) == 0 or pair.get(stk[-1]) != c:
                return False
            else:
                stk.pop()
               
        return True if len(stk) == 0 else False         
                
if __name__ == '__main__':
    s = '[[{}]]{[()()'
    out = Solution()
    print out.isValid(s)
    