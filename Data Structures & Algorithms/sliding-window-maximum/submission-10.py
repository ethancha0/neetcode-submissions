class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        #window boundaries
        left = 0 
        right = 0 

        #monotonic dec order. stores indicies to check OOB 
        queue = deque() 
        ans = [] 


        while right < len(nums): 
            #curr breaks decreasing order 
            while queue and nums[right] > nums[queue[-1]]:
                queue.pop()

            queue.append(right)

            #check if top is OOB 
            if left > queue[0]:
                queue.popleft() 

            
            #append max (first in queue) if window big enough 
            if right-left+1 == k: 
                left += 1 
                ans.append(nums[queue[0]])

            right += 1 

        return ans
        