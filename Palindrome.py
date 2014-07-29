def isPalindrome(s):
    table = 'abcdefghijklmnopqrstuvwxyz'

    lt = []
    for i in s.lower() :
      if i in table or i.isdigit():
         lt.append(i)
    
    if lt == lt[::-1]:
       return True
    else:
        return False
    
if __name__ == '__main__':
    s1 = "A man, a plan, a canal: Panama"
    s2 = "1a2"
    
    print isPalindrome(s1)
    print isPalindrome(s2)