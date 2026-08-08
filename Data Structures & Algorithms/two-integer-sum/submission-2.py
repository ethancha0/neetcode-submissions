class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {} # num:i
        for i in range(len(nums)):
            #check if in hashmap
            complement = target - nums[i]

            if complement not in hashMap: 
                hashMap[nums[i]] = i
            else:
                return([hashMap[complement], i])
                