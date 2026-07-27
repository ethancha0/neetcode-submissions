class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freqMap = {} 
        for t in tasks:
            freqMap[t] = freqMap.get(t, 0) + 1 
        
        maxHeap = [-freq for freq in freqMap.values()]
        heapq.heapify(maxHeap)

        time = 0 
        queue = deque() 

        while queue or maxHeap: 
            #inc time
            time += 1  

            #pop from heap, add to queue
            if maxHeap: 
                count = heapq.heappop(maxHeap)
                if count + 1 < 0:
                    queue.append((count+1, time+n))

            #bring back if time good
            if queue and queue[0][1] == time:
                popped = queue.popleft()
                heapq.heappush(maxHeap, popped[0])

        return time