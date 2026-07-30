class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        # sum of a subarr is prefixsum of end - prefixsum of start+1

        res = 0 
        runningSum = 0 
        prefixSums = {0 : 1} #freqMap: (prefix : count)

        for n in nums: 
            runningSum += n
            target = runningSum - k

            res += prefixSums.get(target, 0)
            
            #add to freqMap
            prefixSums[runningSum] = 1 + prefixSums.get(runningSum, 0)
        
        return res