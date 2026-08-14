class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # use a monotonically decreasing deque to keep track of max in window 
        # only append to ans arr if window size is size k 

        queue = deque() # stores indicies in dec order
        left = 0
        ans = [] 

        for right in range(len(nums)):
            #check if breaks monotonic dec order 
            while queue and nums[right] > nums[queue[-1]]:
                queue.pop() 
            
            queue.append(right)

            #add max to queue once window big enough
            if right-left+1 >= k: 
                ans.append(nums[queue[0]])
                #move left 
                if queue[0] == left: 
                    queue.popleft()
                left += 1 
            

        return ans

