class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # store in freq map 
        freqMap = {}

        for elem in nums: 
            freqMap[elem] = freqMap.get(elem, 0) + 1 

        
        # create bucket 
        bucket = [[] for _ in range(len(nums) + 1)] 

        # fill the bucket 
        for num, count in freqMap.items():
            bucket[count].append(num)

        
        # get the k elem from the end 
        ans = []
        for i in range(len(bucket)-1, -1, -1):

            if len(ans) == k:
                return ans

            for elem in bucket[i]:
                ans.append(elem)

        return ans