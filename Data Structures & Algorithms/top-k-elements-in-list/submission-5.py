class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap = {} 
        for num in nums: 
            freqMap[num] = freqMap.get(num, 0) + 1 

        
        bucket = [[] for _ in range(len(nums)+1) ] 
        for num, freq in freqMap.items(): 
            bucket[freq].append(num) 


        #retrieve k 
        ans = []    
        for i in range(len(bucket)-1, -1, -1):
            for elem in bucket[i]: 
                ans.append(elem)

                if len(ans) == k: 
                    return ans 

