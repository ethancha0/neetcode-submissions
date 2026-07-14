class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0 


        for left in range(len(s)):
            seen = set()
            right = left
            while right < len(s) and s[right] not in seen:
                seen.add(s[right])
                right += 1 
            longest = max(longest, len(seen))

        
        return longest
            