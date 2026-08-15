class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #max profit = highestSell - lowestBuy 

        lowest = float("inf")
        maxProfit = 0

        for p in prices: 
            lowest = min(lowest, p)
            maxProfit = max(maxProfit, p - lowest)

        return maxProfit
