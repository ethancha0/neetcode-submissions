class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        #utilize monotonic decreasing queue 
        #if new window is a max, we can remove all elems in window preceeding

        ans = [] 
        queue = deque() # contains indices
        left = 0 
        right = 0

        while right < len(nums):
            #pop smaller values from queue
            while queue and nums[queue[-1]] <  nums[right]:
                queue.pop()
            queue.append(right)

            # remove left form window if out of bounds
            if left > queue[0]:
                queue.popleft()
            
            #window must be size k
            if (right + 1 ) >= k:
                ans.append(nums[queue[0]])
                left += 1 

            right += 1

        return ans
