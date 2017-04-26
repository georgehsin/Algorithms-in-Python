# Say you have an array for which the ith element is the price of a given stock on day i.

# Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times). However, you may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy = 0
        rp = 0
        profit = 0
        for s in range (1, len(prices)):
            if prices[s] < prices[s-1]:
                buy = s
                profit = 0
            if prices[s] > prices[buy] and prices[s] - prices[buy] > p:
                rp -= profit
                profit = prices[s] - prices[buy]
                rp += profit
        return rp