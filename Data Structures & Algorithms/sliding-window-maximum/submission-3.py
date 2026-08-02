class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        #maintain monotonic dec queue (holds indexs)
        queue = deque() 
        ans = [] 

        #window boundaries
        left = 0 
        right = 0



        while right < len(nums): 
            #check if curr is greater than end of queue 
            while queue and nums[right] > nums[queue[-1]]:
                queue.pop()
            queue.append(right)


            if left > queue[0]: 
                queue.popleft()

            #once window size equal k, append to array
            if right+1 >= k: 
                ans.append(nums[queue[0]])
                left += 1

            right += 1
        
        return ans


        