class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s1) > len(s2):
            return False

        freqMap = {}

        for elem in s1: 
            freqMap[elem] = freqMap.get(elem, 0) + 1
        
        

        left = 0 
        right = len(s1)-1
        window = {} 

        #build initial window 
        for i in range(len(s1)):
            window[s2[i]] = window.get(s2[i], 0) + 1


        while right < len(s2):
            if freqMap == window: 
                return True 
            
            # remove leftmost elem
            window[s2[left]] -= 1

            if window[s2[left]] == 0:
                del window[s2[left]]

            left += 1

            # add rightmost elem 
            right += 1
            if right < len(s2):
                window[s2[right]] = window.get(s2[right], 0) + 1
            
            
        return False





            
