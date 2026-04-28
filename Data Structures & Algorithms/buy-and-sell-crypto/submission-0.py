class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        max_profit = 0
        while l < len(prices) and r < len(prices):
            if prices[r] - prices[l] > max_profit:
                max_profit = prices[r] - prices[l]
            if prices[r] < prices[l]:
                l = r
            r += 1 

        return max_profit