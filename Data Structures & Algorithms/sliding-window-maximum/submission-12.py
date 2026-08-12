class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # since we need to keep track a max given a sliding window, we can use 
        # a monotonically decreasing deque, where the first elem is the largest


        queue = deque() # index:val
        left = 0
        ans = [] 

        #slide
        for i in range(len(nums)):
            while queue and nums[i] >= nums[queue[-1]]:
                queue.pop()
            queue.append(i)

            #move left 
            if left > queue[0]:
                queue.popleft()
            
            if i-left+1 >= k:
                ans.append(nums[queue[0]])
                left += 1
        
        return ans