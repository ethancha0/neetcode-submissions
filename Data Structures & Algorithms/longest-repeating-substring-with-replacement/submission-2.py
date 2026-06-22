class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        #replace the character that is less frequent 

        count = {}
        left = 0 
        longest = 0 


        for right in range(len(s)):
            #build count hash
            if s[right] in count: 
                count[s[right]] += 1
            else:
                count[s[right]] = 1


            #check if window valid 
            # formula: windowsize - most frequent in window
            maxFreq = max(count.values())
            window = right-left+1
            if  window - maxFreq <=  k: # double check this formula 
                longest = max(longest, window)
            else:
                while window  - maxFreq > k: 
                    count[s[left]] -= 1
                    left += 1

                    maxFreq = max(count.values())
                    window = right-left+1
                    
                    

        return longest
        
