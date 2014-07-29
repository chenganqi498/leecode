# Given an input string, reverse the string word by word.

# For example,
# Given s = "the sky is blue",
# return "blue is sky the".

def reverseWords(s):
    lt = s.split(' ')
    new = removeElement(lt, '')  
    return ' '.join(new[::-1])

def removeElement(A, elem):
        j = 0 
        for i in A:
          if i != elem:
            A[j] = i
            j += 1
            
        return A[0:j]
        
if __name__ == '__main__':
    s = "the sky   is blue" 
    out = reverseWords('   ')