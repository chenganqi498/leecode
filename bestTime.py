# Say you have an array i
# for which the ith element is the price of a given stock on day i.

# If you were only permitted to complete at most one transaction 
# (ie, buy one and sell one share of the stock), 
# design an algorithm to find the maximum profit.

class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        if prices == []: return 0
        maxpro = 0
        buy = [prices[0]]
        lowest = prices[0]
        for i in prices[1:]:
            if i < lowest:
               lowest = i
            maxpro = max(maxpro, i - lowest)
        return maxpro
               
if __name__ == '__main__':
   prices = [10,3,5,6,10]
   test = Solution()
   out = test.maxProfit(prices) 
   print out


