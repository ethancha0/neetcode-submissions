class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # max profit = highest day - global min so far 
        globalMin = float("inf")
        bestProfit = 0 
        for elem in prices:
            globalMin = min(globalMin, elem)
            bestProfit = max(bestProfit, elem - globalMin)

        return bestProfit

