class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # 1. build freq map 
        freqMap = {}
        for t in tasks:
            freqMap[t] = freqMap.get(t, 0) + 1 

        # 2. convert into maxheap 
        maxHeap = [-freq for freq in freqMap.values()]
        heapq.heapify(maxHeap)

        # 3. queue and time 
        queue = deque() 
        time = 0 


        while len(queue) > 0 or len(maxHeap) > 0:
            time += 1 

            #bring back from queue to heap 
            if queue and queue[0][1] == time: 
                heapq.heappush(maxHeap, queue.popleft()[0])

            #always pop from heap. heap represents nodes ready to pop
            if maxHeap:
                timeLeft = heapq.heappop(maxHeap) + 1 
                if timeLeft < 0:
                    queue.append((timeLeft, time + n + 1))


        
        return time

            