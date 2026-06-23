class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0 
        count = {} 

        left = 0 
        maxFreq = 0 

        for i in range(len(s)):
            if s[i] in count: 
                count[s[i]] += 1
            else:
                count[s[i]] = 1
        
            maxFreq = max(maxFreq, count[s[i]])

            if (i-left+1) - maxFreq <= k:
                longest = max(longest, (i-left+1))

            while(i-left+1) - maxFreq > k:
                count[s[left]] -= 1
                left += 1
                
            

        return longest