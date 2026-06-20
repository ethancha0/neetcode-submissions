class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        numSets = set(nums) # removes dupes 
        longest = 0

        for elem in numSets: 

            # move if we're at the start of a sequence (no preceding values)
            if elem - 1 in numSets: 
                continue 

            # start of seq atp 
            currStreak = 1 
            currNum = elem + 1

            while currNum in numSets: 
                currStreak += 1
                currNum += 1

            longest = max(longest, currStreak)

        return longest 


            

