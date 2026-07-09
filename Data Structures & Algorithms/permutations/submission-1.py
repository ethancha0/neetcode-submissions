class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        if len(nums) == 0:
            return [[]]

        sliced = self.permute(nums[1:])
        ans = [] 

        for e in sliced: 
            for i in range(len(e)+1):
                temp = e.copy()
                temp.insert(i, nums[0])
                ans.append(temp)
        
        return ans
            
