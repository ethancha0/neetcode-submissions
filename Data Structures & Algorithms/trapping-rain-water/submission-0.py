class Solution:
    def trap(self, height: List[int]) -> int:
        
        prefix = [] 
        leftHighest = 0
        for i in range(len(height)):
            leftHighest = max(leftHighest, height[i]) 
            prefix.append(leftHighest)

        
        suffix = [] 
        rightHighest = 0 
        for i in range(len(height)-1, -1, -1): 
            rightHighest = max(rightHighest, height[i])
            suffix.append(rightHighest)
        suffix.reverse()
        
        water = 0
        for i in range(len(height)): 
            water += min(prefix[i], suffix[i]) - height[i]


        return water