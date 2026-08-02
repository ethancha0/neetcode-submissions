class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        

        #window index boundaries
        left = 0 
        right = 0

        #monotonically inc queue. holds indexs so we can tell when they expire
        queue = deque()
        ans = []

        while right < len(nums): 
            #if curr greater than end, popleft all preceeding 
            while queue and nums[right] > nums[queue[-1]]:
                queue.pop()
            
            queue.append(right)


            #check if front of queue is out of window bounds
            if queue[0] < left: 
                queue.popleft()


            #if window size = k, append front of queue (max), inc left 
            if queue and right-left+1 == k:
                ans.append(nums[queue[0]])
                left += 1 


            right += 1

        return ans
