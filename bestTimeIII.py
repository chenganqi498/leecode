# Say you have an array for which the ith element is the price of a given stock on day i.
# Design an algorithm to find the maximum profit. 
# You may complete at most two transactions.

# Note:
# You may not engage in multiple transactions at the same time 
# (ie, you must sell the stock before you buy again).

class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        if prices == []: return 0
        maxtol, leftmax, rightmax = 0, 0, 0
        left = [] 
        low, high = prices[0], prices[-1]
        for i in range(len(prices)):
            leftmax = max(leftmax, prices[i]-low)
            left.append(leftmax)
            if prices[i] < low: low = prices[i]
        for j in range(len(prices)-1, -1, -1):
            rightmax = max(rightmax, high-prices[j])
            maxtol = max(maxtol, left[j]+rightmax)
            if prices[j] > high: high = prices[j]
        return maxtol
            
if __name__ == '__main__':
   prices = [2,1,4,5,2,9,7]
   test = Solution()
   out = test.maxProfit(prices)
   print out
