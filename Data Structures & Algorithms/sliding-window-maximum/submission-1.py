class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # we can use a max heap to keep track of the max in a given window 

        maxHeap = [] # (val, index)
        ans = [] 


        #build initial heap 
        for i in range(k):
            heapq.heappush(maxHeap, (-nums[i], i))
        #add initial heap to ans 
        ans.append(-maxHeap[0][0])
        
        #slide heap window 
        for i in range(k, len(nums)):

            #add 
            heapq.heappush(maxHeap, (-nums[i], i))

            #check if top index out of bounds 
            while maxHeap[0][1] <= i - k:
                heapq.heappop(maxHeap)

            ans.append(-maxHeap[0][0])


        return ans


