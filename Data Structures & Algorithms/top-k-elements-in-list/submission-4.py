class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #create frequency map
        freqMap = {} 
        for num in nums: 
            freqMap[num] = freqMap.get(num, 0) + 1

        #push values in freqmap as (freq, num) to minHeap 
        minHeap = []
        for num, freq in freqMap.items(): 
            heapq.heappush(minHeap, (-freq, num))


        # get the k most 
        ans = [] 
        for i in range(k):
            ans.append(heapq.heappop(minHeap)[1])

        return ans
  

        
