# Given a string s, 
# partition s such that every substring of the partition is a palindrome.
# Return the minimum cuts needed for a palindrome partitioning of s.

# For example, given s = "aab",
# Return 1 since the palindrome partitioning ["aa","b"] could be produced using 1 cut.

# Exceed time limit, wtf... 
def minCut(s):
    parlen = [0] # min cuts ending at i, now i = 0
    for i in range(1, len(s)+1):
        temp = len(s)  
        for j in range(0, i):                 
            if palindrome(s[j:i]): 
               temp = min(temp, parlen[j])
        parlen.append(temp + 1)                                                      
    return parlen[-1] - 1
                          
def palindrome(sub):
    start = 0
    end = len(sub) - 1
    while sub[start] == sub[end]:
        if end - start <= 1:
            return True
        start += 1
        end -= 1
    return False
        
if __name__ == '__main__':
    s = 'aaabbcaccc'
    out = minCut(s)
        