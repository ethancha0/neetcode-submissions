class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        self.subset = []

        def generate(index):
            if index >= len(nums):
                self.ans.append(self.subset.copy())
                return
            

            #left
            self.subset.append(nums[index])
            generate(index + 1)

            #right 
            self.subset.pop()
            generate(index + 1)

        
        generate(0)
        return self.ans
