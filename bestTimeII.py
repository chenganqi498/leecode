# Say you have an array for which the ith element is the price of a given stock on day i.
# Design an algorithm to find the maximum profit. 
# You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times). 
# However, you may not engage in multiple transactions at the same time 
# (ie, you must sell the stock before you buy again).

class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        if prices == []: return 0
        lowest = prices[0]
        maxpro = 0
        for i in range(len(prices)):
            if prices[i] > lowest: 
               maxpro +=  prices[i]-lowest
            lowest = prices[i]
        return maxpro

if __name__ == '__main__':
   prices = [10,3,5,6,10]
   test = Solution()
   out = test.maxProfit(prices)
   print out

