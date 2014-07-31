# Validate if a given string is numeric.

# Some examples:
# "0" => true
# " 0.1 " => true
# "abc" => false
# "1 a" => false
# "2e10" => true
# Note: It is intended for the problem statement to be ambiguous. 
# You should gather all requirements up front before implementing one.

# Seems tedious but atucally a good practice 
def isNumber(s):
    rmSp = s.split()
    if len(rmSp) != 1:
        return False 
        
    p1 = rmSign(rmSp[0]).isdigit()
    p2 = isFloat(rmSign(rmSp[0]))
    p3 = isScientific(rmSp[0])
       
    return p1 or p2 or p3

def rmSign(s):
    if len(s) > 1:
       if s[0] == '+' or s[0] == '-':
          return s[1:]
    return s
    
def isFloat(s):
    parts = s.split('.')
    if len(parts) == 2 and not (parts[0] == '' and parts[1] == ''):
       if parts[0].isdigit():
           return parts[1].isdigit() or parts[1] == ''
       elif parts[0] == '':
           return parts[1].isdigit()                
    return False
    
def isScientific(s):
    parts = s.split('e')
    if len(parts) == 2:
        parts = [rmSign(parts[0]), rmSign(parts[1])]
        if parts[0].isdigit() or isFloat(parts[0]):
            return parts[1].isdigit()      
    return False
            
if __name__ == '__main__':
    s1 = '0'
    s2 = ' 0.1 '
    s3 = 'abc'
    s4 = '2e10'
    
    print isNumber('+')