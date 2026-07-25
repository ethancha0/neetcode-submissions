class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freqMap = {} 
        for t in tasks: 
            freqMap[t] = freqMap.get(t, 0) + 1 
        
        maxHeap = [-freq for freq in freqMap.values()]
        heapq.heapify(maxHeap)

        queue = deque() 
        time = 0 

        while queue or maxHeap: 
            # inc time
            time += 1 

            # pop from heap 
            if maxHeap: 
                count = heapq.heappop(maxHeap)
                if count + 1 < 0:
                    queue.append((count+1, time+n))



            # bring back if time ready 
            if queue and time == queue[0][1]:
                heapq.heappush(maxHeap, queue.popleft()[0])


        return time