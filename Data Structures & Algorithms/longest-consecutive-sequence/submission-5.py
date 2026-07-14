class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        nSet = set(nums)

        longest = 0 


        for elem in nSet: 
            curr = elem
            streak = 0
            if curr-1 not in nSet:
                while curr in nSet: #start of sequence
                    streak += 1 
                    curr += 1 
                longest = max(longest, streak)

        return longest


        