class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        majority = 0
        majorityFreq = 0

        freqMap = {} 
        for n in nums: 
            freqMap[n] = freqMap.get(n, 0) + 1
            if freqMap[n] > majorityFreq:
                majority = n
                majorityFreq = freqMap[n]

        return majority 