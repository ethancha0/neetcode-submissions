class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        #subarray: two ptr sliding window 
        #abolute difference:  abs(windowMax - windowMin)
        
        # deques should stay monotonic order



        longestWin = 0 
        winMax = deque() # decreasing order (front biggest num) 8, 4
        winMin = deque() # increasing order (front smallest num)
        left = 0 

        for right in range(len(nums)):
            #breaks order: pop all smaller elems 
            while winMax and nums[right] > nums[winMax[-1]]:
                winMax.pop()
            winMax.append(right)
            #breaks order: pop all larger elems 
            while winMin and nums[right] < nums[winMin[-1]]:
                winMin.pop()
            winMin.append(right)


            #check if window is valid 
            while winMin and winMax and abs(nums[winMax[0]] - nums[winMin[0]]) > limit: 
                if winMax[0] == left: 
                    winMax.popleft()
                if winMin[0] == left:
                    winMin.popleft()

                left += 1 
            
            longestWin = max(longestWin, right - left + 1)



        return longestWin
            

            
                

    