class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        nset = set(nums)

        longest = 0 

        for elem in nset: 
            if elem-1 not in nset: 
                curr = elem
                streak = 0 
                while curr in nset: 
                    streak += 1 
                    curr += 1 
                longest = max(longest, streak)
        
        return longest
