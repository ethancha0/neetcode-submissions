class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        longest = 0 
        left = 0
        freqMap = {}
        maxFreq = 0 # tracks how many characters are in the majority 

        for right in range(len(s)): 
            #add to freqMap 
            if s[right] in freqMap: 
                freqMap[s[right]] += 1 
            else: 
                freqMap[s[right]] = 1 

            maxFreq = max(maxFreq, freqMap[s[right]])

            #check if fits within boundaries 
            if right-left+1 -  maxFreq <= k:
                longest = max(longest, right-left+1)

            while right-left+1 - maxFreq > k: 
                freqMap[s[left]] -= 1 
                left += 1 

        
        return longest


            



            
            
