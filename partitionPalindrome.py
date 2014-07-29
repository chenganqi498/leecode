# Given a string s, 
# partition s such that every substring of the partition is a palindrome.
# Return all possible palindrome partitioning of s.

# For example, given s = "aab",
# Return
# [["aa","b"],["a","a","b"]]

# palindromes which end at position i start at walls[j] (a list of start positions)
# all partitions end BEFORE j: par(j)
# for k in walls[j]:
#   par(j) = par(k).append(s[k:j])

def partition(s):
    par = [[[]]]
    for i in range(1, len(s)+1):
        temp = []
        for j in range(0, i):                 
            if palindrome(s[j:i]):                                         
               temp += addOnePalindrome(par[j], s[j:i])
        par.append(temp)  
    return par[-1]

def addOnePalindrome(par, addon):
    new = []
    for i in range(len(par)):
        new.append(par[i] + [addon])
    return new
                          
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
    s = 'aab'
    out = partition(s)
        
    
    