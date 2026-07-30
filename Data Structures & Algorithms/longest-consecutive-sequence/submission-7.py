class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #get rid of dupes putting in a set 
        nSet = set(nums)

        longest = 0 

        for elem in nSet: 
            #check if start of a sequence
            curr = elem
            streak = 1 
            while curr+1 in nSet:
                streak += 1
                curr += 1
            longest = max(longest, streak)

        return longest


