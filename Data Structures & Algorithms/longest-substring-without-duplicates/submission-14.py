class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #hash set 
        winSet = set() 

        left = 0 
        right = 0
        longest = 0

        while right < len(s): 
            while s[right] in winSet: 
                winSet.remove(s[left])
                left += 1 


            #reset
            longest = max(longest, right-left+1)
            winSet.add(s[right])
            right += 1


        return longest
