class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        runningCount = 0 
        ans = 0 
        hashMap = {0:1} # prefix:count

        for n in nums: 
            #add to runningCount 
            runningCount += n 

            #check for target 
            target = runningCount - k
            
            #check if in hashMap 
            ans += hashMap.get(target, 0)

            #add to hashMap 
            hashMap[runningCount] = hashMap.get(runningCount, 0) + 1

        return ans