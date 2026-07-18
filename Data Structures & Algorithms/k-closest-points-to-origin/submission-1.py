class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        #create a 'window' or heap of size k 
        maxHeap = [] 
        heapq.heapify(maxHeap)

        for x, y in points: 
            distance = x*x + y*y
            heapq.heappush(maxHeap, (-1 * distance, (x, y)))
            
            while len(maxHeap) > k: 
                heapq.heappop(maxHeap)

        return [item[1] for item in maxHeap]
                