class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        mySet = set() 

        for elem in nums: 
            if elem in mySet: 
                return True
            else: 
                mySet.add(elem)

        return False
        

        