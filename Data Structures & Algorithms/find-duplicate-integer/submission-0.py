class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # fast/slow pointers

        freqMap = {} 
        for elem in nums:
            if elem in freqMap: 
                return elem
            else:
                freqMap[elem] = 1
        