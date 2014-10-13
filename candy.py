# There are N children standing in a line. 
# Each child is assigned a rating value.

# You are giving candies to these children 
# subjected to the following requirements:

# Each child must have at least one candy.
# Children with a higher rating get more candies than their neighbors.
# What is the minimum candies you must give?

# Do not understand why it expects 4:
# Input:	[1,2,2]
# Output:	5
# Expected:	4

class Solution:
    # @param ratings, a list of integer
    # @return an integer
    def candy(self, ratings):
        lr = len(ratings)
        peak, bottom = 0, 0
        tol, indiv = 0, 0
        for i in range(lr):
            if i == 0 or ratings[i] > ratings[i-1]:
               indiv += 1
            elif ratings[i] < ratings[i-1]:
               indiv -= 1
            if (i == 0 or ratings[i] < ratings[i-1]) and\
               (i == lr-1 or ratings[i] < ratings[i+1]):
               tol += (1-indiv)*(i-peak) #correction
               indiv = 1
            elif (i == 0 or ratings[i] > ratings[i-1]) and\
               (i == lr-1 or ratings[i] > ratings[i+1]):
               peak = i
            tol += indiv
        return tol

if __name__ == '__main__':
   ratings = [1,3,5,7,9,5,0]
   test = Solution()
   out = test.candy(ratings)
   print out
