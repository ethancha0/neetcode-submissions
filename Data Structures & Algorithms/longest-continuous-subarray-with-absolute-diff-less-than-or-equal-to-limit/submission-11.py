class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        # we need to keep track of max/min of window 
        greatest = deque() #monotonically decreasing
        smallest = deque() #monotonically increasing

        left = 0
        largest = 0

        for right in range(len(nums)): 
            #check max
            while greatest and nums[right] > nums[greatest[-1]]:
                greatest.pop()
            greatest.append(right)


            #check min
            while smallest and nums[right] < nums[smallest[-1]]:
                smallest.pop() 
            smallest.append(right)


            #move window if needed
            if abs(nums[greatest[0]] - nums[smallest[0]]) > limit:
                if left == greatest[0]:
                    greatest.popleft()
                if left == smallest[0]:
                    smallest.popleft()
                
                left += 1

            #calculate
            largest = max(largest, right-left+1)
                

            
        return largest

