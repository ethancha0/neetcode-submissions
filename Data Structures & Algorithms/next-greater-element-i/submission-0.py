class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        # find next greatest neigh for nums2. put in a hashmap then retrieve for nums1

        ans = []

        stack = [] #monotonic decreasing
        nextGreatest = {} 

        for i in range(len(nums2)): 
            while stack and nums2[i] > stack[-1][0]:
                value, index = stack.pop()
                nextGreatest[value] = nums2[i]
            
            stack.append((nums2[i], i))

        
        #search in hash 
        for n in nums1: 
            ans.append(nextGreatest.get(n, -1))



        return ans
            
