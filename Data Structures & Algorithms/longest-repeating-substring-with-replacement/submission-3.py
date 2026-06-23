class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        

        longest = 0 
        left = 0 
        maxFreq = 0
        hashMap = {} # stores freq 

        for i in range(len(s)):
            # add frequencies 
            if s[i] in hashMap:
                hashMap[s[i]] += 1
            else: 
                hashMap[s[i]] = 1
            
            maxFreq = max(maxFreq, hashMap[s[i]])

            # formula: windowSize - mostFreqElem <= k
            if (i - left + 1) - maxFreq > k:
                hashMap[s[left]] -= 1
                left += 1

            longest = max(longest, i - left + 1)
            
        
        return longest
