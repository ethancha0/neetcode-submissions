class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        # heap: distance, (x, y)
        # min heap of size k

        minHeap = [] 
        for x, y in points: 
            distance = x*x + y*y
            heapq.heappush(minHeap, (-distance, (x, y)))

            if len(minHeap) > k: 
                heapq.heappop(minHeap)

        ans = [] 
        for d, coord in minHeap: 
            ans.append(coord)
        
        return ans

        
