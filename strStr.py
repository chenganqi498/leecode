# Implement strStr().
# Returns a pointer to the first occurrence of needle in haystack, 
# or null if needle is not part of haystack.

def strStr(haystack, needle):
    hlen = len(haystack)
    nlen = len(needle)
    i = 0

    while i <= hlen - nlen:
        overlapped = compare(haystack[i:i + nlen], needle, nlen)
        if overlapped == nlen:
            return haystack[i:]
        elif overlapped == 0:
            i += 1
        else: 
            partial = matchTable(haystack[i:i+overlapped])
            i += overlapped - partial  
                  
    return None

def matchTable(s):
    l = len(s)
    if l <= 1: return 0         
    maxlen = 0
    
    for i in range(1,l):
        if s[0:i] == s[l-i:l]:
           maxlen = i
                       
    return maxlen

# assume two strings have same lengthout
def compare(s1, s2, length): 
    count = 0
    for i in range(length):
        if s1[i] == s2[i]:
            count += 1
        else:
            break
    return count
   
if __name__ == '__main__':
    haystack = 'BBC ABCDAB ABCDABCDABDE'
    needle = 'ABCDABE'
    
    out = strStr('mississippi', 'issip')