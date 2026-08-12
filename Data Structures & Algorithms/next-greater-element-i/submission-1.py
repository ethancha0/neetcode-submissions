class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # monotonic decreasing stack 
        stack = [] # (value, index)
        hashMap = {} 

        for i, n in enumerate(nums2): 
            while stack and n > stack[-1][0]:
                value, index = stack.pop()
                hashMap[value] = n
        
            stack.append((n, i))
        

        #add and check 
        ans = []
        for n in nums1:
            ans.append(hashMap.get(n, -1))
        
        return ans
            