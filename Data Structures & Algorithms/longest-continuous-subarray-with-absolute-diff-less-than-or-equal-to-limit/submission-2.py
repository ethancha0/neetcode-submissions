class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        
        # store indicies
        largest = deque() #monotonic decreasing
        smallest = deque() #monotonic increasing

        left = 0
        largestWin = 0

        for right in range(len(nums)):
            
            #breaks order of largest
            while largest and nums[right] > nums[largest[-1]]:
                largest.pop()
            largest.append(right)


            #breaks order of left
            while smallest and nums[right] < nums[smallest[-1]]:
                smallest.pop()
            smallest.append(right)


            if abs(nums[largest[0]] - nums[smallest[0]]) > limit: 
                if left == largest[0]:
                    largest.popleft()
                if left == smallest[0]:
                    smallest.popleft()
                left += 1

            #check and adjust window
            largestWin = max(largestWin, right-left+1)
            

        return largestWin

            
            