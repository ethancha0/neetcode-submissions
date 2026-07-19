class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [] 
        for stone in stones: 
            maxHeap.append(-1 * stone)
        heapq.heapify(maxHeap)

        while len(maxHeap) > 1: 
            o1 = heapq.heappop(maxHeap)
            o2 = heapq.heappop(maxHeap) 
            if o1 != o2: 
                heapq.heappush(maxHeap, o1 - o2)

        if maxHeap: 
            return -maxHeap[0] 
        return 0 