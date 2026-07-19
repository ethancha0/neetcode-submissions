class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = [] 
        heapq.heapify(maxHeap)

        for x, y in points: 
            distance = x*x + y*y
        
            heapq.heappush(maxHeap, (-distance, (x,y))) 
            while len(maxHeap) > k: 
                heapq.heappop(maxHeap) 

        return [item[1] for item in maxHeap]