class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        #elem:freq
        freqMap = {} 

        for n in nums: 
            freqMap[n] = freqMap.get(n, 0) + 1 

        
        #sort into buckets. group elems with same freq 
        buckets = [[] for _ in range(len(nums) + 1)] # add +1 for the elems with 0 freq? 
        for elem, freq in freqMap.items(): 
            buckets[freq].append(elem)

        #iterate from back 
        ans = [] 
        for i in range(len(buckets)-1, -1, -1):
            for elem in buckets[i]: 
                ans.append(elem)

            if len(ans) == k:
                break



        return ans 
