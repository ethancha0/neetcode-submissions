class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        #window boundaries 
        left = 0 
        right = 0 

        #monotonic dec queue. stores indicies so we can check if out of bounds 
        queue = deque()
        ans = [] 

        while right < len(nums): 
            #if curr elem is greater than queue end, del all preceeding 
            while queue and nums[right] > nums[queue[-1]]:
                queue.pop() 

            queue.append(right)

            #check if front is out of bounds 
            if left > queue[0]: 
                queue.popleft() 

            #append max of window
            if right-left+1 == k:
                ans.append(nums[queue[0]])
                left += 1 

            right += 1 

        return ans
