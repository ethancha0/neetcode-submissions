class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #hashmap: {num:index}
        hashMap = {} 

        for i, n in enumerate(nums): 
            complement = target - n
            if complement in hashMap: 
                return[hashMap[complement], i]
            else: 
                hashMap[n] = i 

        