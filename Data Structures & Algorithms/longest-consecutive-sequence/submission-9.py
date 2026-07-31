class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #for each elem, check if its the start of new list

        #remove duplicates w set 
        nums = set(nums)

        longest = 0 

        for n in nums: 
            if n-1 not in nums:
                streak = 0
                curr = n
                while curr in nums: 
                    streak += 1
                    curr += 1
                longest = max(longest, streak)

        return longest