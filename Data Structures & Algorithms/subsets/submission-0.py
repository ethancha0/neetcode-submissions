class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        subset= [] 

        def backtrack(index):
            if index == len(nums): # reached end of array
                res.append(subset.copy())
                return res


            # decision 1: include 
            subset.append(nums[index])
            backtrack(index + 1)

            subset.pop()

            # decision 2: exclude
            backtrack(index + 1)

        
        backtrack(0)
        return res

  