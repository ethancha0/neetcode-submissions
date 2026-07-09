class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        if len(nums) == 0:
            return [[]]

        sliced = self.permute(nums[1:])

        ans = []

        for subarray in sliced: 
            for i in range(len(subarray)+1):
                temp = subarray.copy()
                temp.insert(i, nums[0])
                ans.append(temp)
        
        return ans 
