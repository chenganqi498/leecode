# Given n pairs of parentheses, 
# write a function to generate all combinations of well-formed parentheses.

# For example, given n = 3, a solution set is:
# "((()))", "(()())", "(())()", "()(())", "()()()"

def generateParenthesis(n):
    root = ['()'] 
    for count in range(n-1):
        new = []
        for i in root:
            new += addOneParenthesis(i)
        root = list(set(new))
    return root
 
def addOneParenthesis(old):
    new = []   
    for i in range(len(old)-1):
        if old[i] == '(' and old[i+1] == ')':
            leftchild = old[0:i] + '()()' + old[i+2:]
            rightchild = old[0:i] + '(())' + old[i+2:]
            new.append(leftchild)
            new.append(rightchild)         
    return new             
                
if __name__ == '__main__':
    root = ['()']
    count = 0  
    out = generateParenthesis(4)
    