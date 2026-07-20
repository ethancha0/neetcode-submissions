class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap = {} 
        for num in nums: 
            freqMap[num] = freqMap.get(num, 0) + 1 
        
        # build bucket 
        bucket = [[] for _ in range(len(nums)+1)] 
        for index, value in freqMap.items(): 
            bucket[value].append(index)
        

        # slice k from end 
        ans = [] 
        for i in range(len(bucket)-1, -1, -1):
            for elem in bucket[i]:
                ans.append(elem)

                if len(ans) == k:
                    return ans
        