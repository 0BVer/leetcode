class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        all, p, mi = 0, 0, prices[0]

        for i in range(1, len(prices)):
            if p < prices[i] - mi:
                p = prices[i] - mi
            if prices[i] < prices[i - 1] or i == len(prices) - 1:
                all += p
                p = 0
                mi = float('inf')
            if prices[i] < mi:
                mi = prices[i]
        
        return all