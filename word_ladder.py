# Given two words (start and end), and a dictionary, 
# find the length of shortest transformation sequence from start to end, 
# such that:
# 1.Only one letter can be changed at a time
# 2.Each intermediate word must exist in the dictionary

# @param start, a string
# @param end, a string
# @param d, a set of string
# @return an integer
    
def ladderLength(start, end, d):
    length = 1
    ladder = [start]
     
    while ladder != []:
       children = []
       
       for word in ladder:
           children += nextLevel(word, d)
      
       for word in children:
           if compareString(word, end):
               return length + 2
           
       length += 1
       ladder = children
            
    return 0
 
def nextLevel(word, d):
    temp = []
    for item in d:
        if compareString(word, item):
            temp.append(item)
            d.remove(item)
    return temp
                    
def compareString(s1, s2):
    count = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            count += 1
        if count > 1:
            return False
 
    if count == 1:
        return True
        
if __name__ == '__main__':
    d = ['hot', 'dot', 'dog', 'lot', 'log']
    print ladderLength('hit', 'cog', d)