# Given two words word1 and word2, 
# find the minimum number of steps required to convert word1 to word2. 
# (each operation is counted as 1 step.)

# You have the following 3 operations permitted on a word:

# a) Insert a character
# b) Delete a character
# c) Replace a character

class Solution:
    # @return an integer
    def minDistance(self, word1, word2):
        l1, l2 = len(word1), len(word2)
        if l1 == 0: return l2
        if l2 == 0: return l1
        
        # dist[i][0] = i, dist[0][j] = j
        dist = [[0]*(l2+1) for i in range(l1+1)]
        for i in range (l1+1): dist[i][0] = i 
        for j in range(l2+1): dist[0][j] = j
        
        for i in range(l1):
            for j in range(l2):
                if word1[i] == word2[j]:
                    dist[i+1][j+1] = dist[i][j]
                else:
                    dist[i+1][j+1] = min(dist[i][j+1], dist[i+1][j], dist[i][j]) + 1
                    
        return dist[l1][l2]
              
            
if __name__ == '__main__':
    word1, word2 = "distance", "springbok" 
    test = Solution()
    out = test.minDistance(word1, word2)