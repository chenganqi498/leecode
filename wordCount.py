def wordCount(s):
    dictionary = {}
    
    for i in s:
        if dictionary.get(i) == None:
            dictionary[i] = 1
        
        else: dictionary[i] += 1
    
    return dictionary
    
if __name__ == '__main__':
    s = ['abd', 'c', 'pp','abc', 'c','pp','pp']
    cc = wordCount(s)