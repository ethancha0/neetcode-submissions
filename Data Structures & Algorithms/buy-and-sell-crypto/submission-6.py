class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # maxProfit = highest day (current) - lowest day (past) 

        lowest = float('inf')
        maxProfit = 0

        for p in prices: 
            lowest = min(lowest, p)
            maxProfit = max(maxProfit, p-lowest)

           

        return maxProfit