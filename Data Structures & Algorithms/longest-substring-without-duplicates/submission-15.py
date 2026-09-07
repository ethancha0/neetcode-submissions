class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #substring => slinding window 
        #no duplicates => set 

        winSet = set()
        longestWin = 0

        left = 0 

        for right in range(len(s)):
            while s[right] in winSet:
                winSet.remove(s[left])
                left += 1
            
            winSet.add(s[right])
            longestWin = max(longestWin, right-left+1)

        return longestWin

