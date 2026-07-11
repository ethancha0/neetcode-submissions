class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # convert to set to remove dupes
        nset = set(nums) 
        longest = 0 

        # check if start of a sequence 
        for elem in nset: 
            #first of a sequence
            if elem-1 not in nset: 
                streak = 0
                start = elem

                while start in nset: 
                    streak += 1 
                    start += 1
                
                longest = max(longest, streak)

        
        return longest
                
