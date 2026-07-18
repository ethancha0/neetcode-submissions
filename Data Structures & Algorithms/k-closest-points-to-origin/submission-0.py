class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        #create a 'window' or heap of size k 
        maxHeap = [] 
        heapq.heapify(maxHeap)

        for p in points: 
            x1, y1 = p
            heapq.heappush(maxHeap, (-1 * math.sqrt(x1*x1 + y1*y1), (x1,y1)) )
            
            while len(maxHeap) > k: 
                heapq.heappop(maxHeap)

        return [item[1] for item in maxHeap]
                