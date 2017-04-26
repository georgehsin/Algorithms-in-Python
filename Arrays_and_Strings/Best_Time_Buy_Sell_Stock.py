# Say you have an array for which the ith element is the price of a given stock on day i.

# If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy = 0
        profit = 0
        for x in range(1,len(prices)):
            if prices[x] < prices[buy]:
                buy = x
            elif prices[x] - prices[buy] > profit:
                profit = prices[x] - prices[buy]
        return profit
            