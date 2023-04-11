class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1: return 0
        min_buy = min(prices[0], prices[1])
        p = max(0, prices[1] - prices[0])

        for i in range(2, len(prices)):
            min_buy = min(min_buy, prices[i - 1])
            p = max(p, prices[i - 1] - prices[i - 2], prices[i] - min_buy)
        return p