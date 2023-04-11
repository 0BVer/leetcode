class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1: return 0
        min_buy = prices[0]
        p = 0

        for i in range(1, len(prices)):
            if min_buy > prices[i - 1]:
                min_buy = prices[i - 1]
            if p < prices[i] - min_buy:
                p = prices[i] - min_buy
        return p