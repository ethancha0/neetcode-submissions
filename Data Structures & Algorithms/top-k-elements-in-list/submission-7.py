class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # bucket sort 
        # first freq map, then put the highest freq into buckets. 
        # freqMap: elem:freq
        # bucket: freq:elems

        freqMap = {}
        for n in nums: 
            freqMap[n] = freqMap.get(n, 0) + 1 

        buckets = [[] for _ in range(len(nums)+1)] # +1 to accomadate for 0?
        for elem, freq in freqMap.items(): 
            buckets[freq].append(elem)
            

        
        #append end buckets to ans 
        ans = [] 
        for i in range(len(buckets)-1, -1, -1):
            for elem in buckets[i]:
                ans.append(elem)

            if len(ans) == k:
                return ans