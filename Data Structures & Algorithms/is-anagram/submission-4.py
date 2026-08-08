class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #freqmap 
        sMap = {}
        for elem in s: 
            sMap[elem] = sMap.get(elem, 0) + 1 

        #compare against t 
        for elem in t: 
            if not elem in sMap: 
                return False
            else: 
                sMap[elem] -= 1 
                if sMap[elem] == 0: 
                    del sMap[elem]
        
        return len(sMap) == 0