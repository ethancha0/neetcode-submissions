class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # hashMap => key: num, val: freq
        hashMap = {}

        for elem in nums: 
            if elem in hashMap: 
                hashMap[elem] += 1 
            else: 
                hashMap[elem] = 1 


        # bucket sort 
        bucket = [[] for _ in range(len(nums)+1)]

        # fill bucket (double check this )
        for num, freq in hashMap.items(): 
            bucket[freq].append(num)
        

        # get the k most (end)
        ans = []
        for i in range(len(bucket)-1, -1, -1):
            for elem in bucket[i]:
                ans.append(elem)
            if len(ans) == k: 
                return ans

         
