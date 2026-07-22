class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap = [] 

        for elem in nums: 
            heapq.heappush(minHeap, elem)

            if len(minHeap) > k: 
                heapq.heappop(minHeap)

        return minHeap[0]