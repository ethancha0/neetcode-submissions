class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-s for s in stones]
        heapq.heapify(maxHeap)

        while len(maxHeap) > 1:
            o1 = heapq.heappop(maxHeap)
            o2 = heapq.heappop(maxHeap)
            if o1 != o2:
                heapq.heappush(maxHeap, o1 - o2)
        
        if maxHeap: 
            return -1 * maxHeap[0]
        return 0