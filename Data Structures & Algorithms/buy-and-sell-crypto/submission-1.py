class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        min_price = float('inf')
        max_prof = 0
        for i in range(len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            if prices[i] - min_price > max_prof:
                max_prof = prices[i] - min_price
        return max_prof