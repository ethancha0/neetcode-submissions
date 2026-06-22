class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        mySet = set() 
        longest = 0
        left = 0  # start of substring


        for right in range(len(s)):  # right: end of substring
            while s[right] in mySet: 
                mySet.remove(s[left])
                left += 1
                

            
            mySet.add(s[right])

            longest = max(longest, right-left+1)

        return longest
            


        