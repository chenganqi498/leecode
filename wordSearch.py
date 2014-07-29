# Given a 2D board and a word, find if the word exists in the grid.

# The word can be constructed from letters of sequentially adjacent cell, 
# where "adjacent" cells are those horizontally or vertically neighboring. 
# The same letter cell may not be used more than once.

# For example,
# Given board =
# ["ABCE",
#  "SFCS",
#  "ADEE"]
# word = "ABCCED", -> returns true,
# word = "SEE", -> returns true,
# word = "ABCB", -> returns false.

def exist(board, word):
    pointer = 1
    
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == word[0]:
                if len(word) == 1:
                    return True
                if search(board, word, [i,j], pointer, [[i,j]]):
                    return True
    return False

def search(board, word, loc, pointer, tracker): 
    out = False
    directions = [[1,0], [-1,0], [0,1], [0,-1]] 
     
    # boundary conditions
    if loc[0] == 0:
        directions.remove([-1,0])
    if loc[0] == len(board)-1:
        directions.remove([1,0])
    if loc[1] == 0:
        directions.remove([0,-1])
    if loc[1] == len(board[0]) - 1:
        directions.remove([0,1])
    
    for [dx, dy] in directions: 
        newtracker = tracker
        newloc = [loc[0]+dx, loc[1]+dy]   
        if newloc not in tracker and board[newloc[0]][newloc[1]] == word[pointer]:    
            newtracker = tracker + [newloc]
            newpointer = pointer + 1  
            if newpointer == len(word):
               return True         
            out = search(board, word, newloc, newpointer, newtracker) 
        if out == True:
            break     
                  
    return out
            
if __name__ == '__main__':
    board =["ABCE","SFCS","ADEE"]
    word1 = "ABCCED"
    word2 = "SEE"
    word3 = "ABCB"
   
    out = exist(board, word3)
    
    