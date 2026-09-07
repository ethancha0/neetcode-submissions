class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        freqMap = {}

        #find out which is majority 
        # we don't actually need to 'replace', we just need to see if the freq of the maj elem + k < windowsize

        left = 0 
        for right in range(len(s)):
            freqMap[s[right]] = freqMap.get(s[right], 0) + 1
            while right-left+1 > max(freqMap.values()) + k:
                freqMap[s[left]] -= 1
                left += 1 
            
            longest = max(longest, right-left+1)

        return longest
