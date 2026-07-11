class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        globalMin = prices[0]
        best = 0 

        for e in prices: 
            best = max(best, e-globalMin)
            globalMin = min(globalMin, e)

        return best
            
