class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # bucket sort: first build freqmap 

        freqMap = {} 
        for n in nums: 
            if n not in freqMap: 
                freqMap[n] = 0
            freqMap[n] += 1 
        
        #bucket: indicies will hold values of that freq 
        bucket = [[] for _ in range(len(nums)+1)]
        for num, freq in freqMap.items(): 
            bucket[freq].append(num)
        
        #get the elems from the end 
        ans = []
        for i in reversed(range(len(bucket))):
            for elem in bucket[i]:
                ans.append(elem)

                if len(ans) == k:
                    return ans 