class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0: 
            return [[]]

        sub = self.permute(nums[1:])

        ans = []

        for subArray in sub:
            for i in range(len(subArray)+1):
                temp = subArray.copy()
                temp.insert(i, nums[0])
                ans.append(temp)

        return ans
                