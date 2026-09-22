class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        res = 0
        
        for right in range(len(prices)):
            current_profit = prices[right] - prices[left]
            while current_profit < 0:
                left += 1
                current_profit = prices[right] - prices[left]
            res = max(res, current_profit)
        return res
            