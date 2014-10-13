# Given a collection of integers that might contain duplicates, S, 
# return all possible subsets.

# Note:
# Elements in a subset must be in non-descending order.
# The solution set must not contain duplicate subsets.

# For example,
# If S = [1,2,2], a solution is:
# [[2],
#  [1],
#  [1,2,2],
#  [2,2],
#  [1,2],
#  []]

# DP!
class Solution:
    # @param S, a list of integer
    # @return a list of lists of integer
    def subsetsWithDup(self, S):
        out = [[]]
        S.sort()
        for i in range(len(S)):
            temp = []
            for item in out:
                add = item+[S[i]]
                if add not in out and add not in temp: temp.append(add)
                for j in range(1,len(item)):
                    if j > 0 and item[j] == item[j-1]:continue
                    if item[j] == S[i]: continue
                    rep = item[0:j] + item[j+1:] + [S[i]]
                    if rep not in out and add not in temp: temp.append(rep)
            out += temp
        return out
    
if __name__ == '__main__':
    S = [1,2,3,4,5,6,7,8,10,0]
    test = Solution()
    out = test.subsetsWithDup(S)
    print out
