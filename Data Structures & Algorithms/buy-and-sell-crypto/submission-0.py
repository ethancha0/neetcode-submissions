class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        globalMin = prices[0]
        maxProfit = 0 
        # find the max - min 
        # but the max has to come after the min 

        for elem in prices: 
            globalMin = min(globalMin, elem)
            maxProfit = max(maxProfit, elem-globalMin)
        


        return maxProfit