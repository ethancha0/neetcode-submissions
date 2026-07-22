class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        hashMap = {}
        longest = 0

        left = 0 
        for right in range(len(s)): 

            if s[right] in hashMap: 
                hashMap[s[right]] += 1
            else: 
                hashMap[s[right]] = 1

            #check if majority
            while (right-left+1) - max(hashMap.values()) > k:
                hashMap[s[left]] -= 1 
                if hashMap[s[left]] == 0:
                    del hashMap[s[left]]
                left += 1 
            
            longest = max(longest, right-left+1)

        return longest
