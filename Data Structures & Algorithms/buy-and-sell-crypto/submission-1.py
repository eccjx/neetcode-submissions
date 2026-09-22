class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        l = 0
        for i in range(len(prices)):
            current_profit_at_i = prices[i] - prices[l]
            if current_profit_at_i < 0:
                l = i
            res = max(res, current_profit_at_i)
        return res