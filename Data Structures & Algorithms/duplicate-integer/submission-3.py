class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set() 

        for n in nums: 
            if not n in seen: 
                seen.add(n)
            else: 
                return True
        
        return False
