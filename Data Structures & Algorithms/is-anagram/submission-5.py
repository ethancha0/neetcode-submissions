class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #store s in freqMap, compare against t 
        sMap = {} 

        for elem in s: 
            sMap[elem] = sMap.get(elem, 0) + 1 
        
        
        #compare against t 
        for elem in t: 
            if elem not in sMap: 
                return False 
            
            sMap[elem] -= 1
            if sMap[elem] == 0: 
                del sMap[elem]
        
        return len(sMap) == 0