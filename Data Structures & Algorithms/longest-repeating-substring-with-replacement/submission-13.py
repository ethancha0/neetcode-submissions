class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0 
        majority = 0 
        left = 0 
        freqMap = {} 

        for right in range(len(s)): 
            freqMap[s[right]] = freqMap.get(s[right], 0) + 1 

            majority = max(majority, freqMap[s[right]])
    
            #calc window : window - majority = minority
            while right-left+1 - majority > k: 
                freqMap[s[left]] -= 1 
                left += 1 
            
            longest = max(longest, right-left+1)

        
        return longest
