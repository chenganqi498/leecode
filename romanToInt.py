# Given a roman numeral, convert it to an integer.

# Input is guaranteed to be within the range from 1 to 3999.

def romanToInt(s):
    table = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    Int = 0
    i = 0
   
    while i < len(s)-1:
        if table[s[i]] <table[s[i+1]]:
            Int += table[s[i+1]] - table[s[i]]
            i += 2
        else:
            Int += table[s[i]]
            i += 1
        
    if i == len(s):
        return Int
    else:
        return Int + table[s[i]]
    
if __name__ == '__main__':
    s = 'MDCCCLXXXIV'
    out = romanToInt(s)
        
        