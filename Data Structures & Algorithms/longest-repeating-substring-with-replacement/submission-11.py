class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        longest = 0 
        freqMap = {} 
        left = 0 
        maxFreq = 0

        for right in range(len(s)):

            if s[right] in freqMap:
                freqMap[s[right]] += 1
            else: 
                freqMap[s[right]] = 1


            maxFreq = max(maxFreq, freqMap[s[right]])
            
            if right-left+1 - maxFreq <= k: 
                longest = max(longest, right-left+1)
            
            while right-left+1 - maxFreq > k:
                freqMap[s[left]] -= 1 
                left += 1


        return longest 

