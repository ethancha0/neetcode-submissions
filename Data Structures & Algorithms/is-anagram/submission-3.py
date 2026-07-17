class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freqMap = {} 
        for elem in s: 
            freqMap[elem] = freqMap.get(elem, 0) + 1
        
        for elem in t: 
            if elem in freqMap:
                freqMap[elem] -= 1 
                if freqMap[elem] == 0: 
                    del freqMap[elem]
            else:
                return False 
            
        if len(freqMap) == 0: 
            return True
        else: 
            return False