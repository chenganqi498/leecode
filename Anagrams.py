# Given an array of strings, return all groups of strings that are anagrams.

# Note: All inputs will be in lower-case.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        
def anagrams(strs):
    table = dict()
    headtable = []
    group = []
    
    for i in range(len(strs)):
        new = str(sorted(strs[i]))
        if new not in table:
            table[new] = ListNode(i)
            trace = table[new]
            headtable.append(trace)         
        else:
            table[new].next = ListNode(i)
            table[new] = table[new].next
        
    for head in headtable:
        if head.next != None:
            group += listToArray(head, strs)
    
    return group
        
def listToArray(head, strs):
    array = []
    while head != None:
        array.append(strs[head.val])
        head = head.next
    return array

if __name__ == '__main__':
    s1 = ['abcd', 'efgh', 'bcda','egfh', 'effg']
    s2 = ['', 'a', '']
    out = anagrams(s1)