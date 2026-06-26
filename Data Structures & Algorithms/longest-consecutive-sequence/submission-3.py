class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        numsSet = set(nums)

        longest = 0 

        for elem in numsSet:

            if elem-1 in numsSet: 
                continue

            streak = 0
            curr = elem 
            while curr in numsSet: 
                streak += 1
                curr += 1
            
            longest = max(longest, streak)
        
        return longest