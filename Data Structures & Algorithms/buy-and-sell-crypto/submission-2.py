class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        globalMin = prices[0]
        bestProfit = 0

        for i in range(len(prices)):
            globalMin = min(globalMin, prices[i])
            bestProfit = max(bestProfit, prices[i] - globalMin)

        return bestProfit

