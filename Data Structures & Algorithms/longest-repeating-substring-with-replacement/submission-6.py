class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        hashMap = {}
        left = 0
        mostFreq = 0
        longest = 0 

        for i in range(len(s)):
            if s[i] in hashMap: 
                hashMap[s[i]] += 1
            else:
                hashMap[s[i]] = 1 

            mostFreq = max(mostFreq, hashMap[s[i]])

            # formula: smallElem = window - most freq  
            if (i - left + 1) - mostFreq <= k:
                longest = max(longest, (i-left+1))
                
            while (i - left + 1) - mostFreq > k: 
                hashMap[s[left]] -= 1 
                left += 1
                

        return longest
            
        
        