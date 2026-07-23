class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # freq map 
        freqMap = {} 
        for t in tasks: 
            freqMap[t] = freqMap.get(t, 0) + 1 

        # convert freq into max heap 
        maxHeap = [-freq for freq in freqMap.values()]
        heapq.heapify(maxHeap)

        queue = deque() 
        time = 0 

        while queue or len(maxHeap) > 0:

            # add time 
            time += 1 


            # pop from maxheap + add to queue if val > 0
            if len(maxHeap) > 0:
                popped = heapq.heappop(maxHeap)
                if popped + 1 < 0:
                    queue.append((popped + 1, time + n))

            # bring back from queue time time ready
            if queue and queue[0][1] == time: 
                heapq.heappush(maxHeap, queue.popleft()[0])



        return time
