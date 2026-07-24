class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # freq map 
        freqMap = {} 
        for t in tasks: 
            freqMap[t] = freqMap.get(t, 0) + 1 

        # max heap 
        maxHeap = [-freq for freq in freqMap.values()]
        heapq.heapify(maxHeap)


        queue = deque() 
        time = 0 

        while queue or maxHeap: 

            # inc time 
            time += 1

            # pop from maxheap
            if len(maxHeap) > 0:
                temp = heapq.heappop(maxHeap) 
                if temp + 1 < 0: 
                    queue.append((temp+1, time+n))

            # bring back if time is ready 
            if queue and queue[0][1] == time:
                heapq.heappush(maxHeap, queue.popleft()[0])
                



        return time