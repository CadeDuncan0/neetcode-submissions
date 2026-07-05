class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxP = 0

        while r < len(prices):
            # only check for profit if left is buy is less than sell
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            # only move buy if it is greater than sell
            else:
                l = r
            r += 1
        return maxP