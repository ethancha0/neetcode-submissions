class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # use monotonic decreasing deque to keep track of max in given window
        # only add to ans array once window is big enough 

        left = 0 
        queue = deque() # indicies
        ans = [] 

        for right in range(len(nums)): 
            while queue and nums[right] > nums[queue[-1]]:
                queue.pop() 
            queue.append(right)


            #move left and add max once window is big enough
            if right-left+1 >= k:

                ans.append(nums[queue[0]])

                if left == queue[0]:
                    queue.popleft() 
                left += 1 

        return ans
            
