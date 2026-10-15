class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #permutation: order doesn't  matters 
        #s1 must be a subset of s2 

        #use sliding window, keep freq map of the sliding window. 
        #if the freqmap of the sliding window matches s1. return true 

        if len(s2) < len(s1): 
            return False


        map1 = {} 
        for elem in s1: 
            map1[elem] = map1.get(elem, 0) + 1 

        front = 0 
        end = len(s1) -1
        winMap = {} 
        
        #fill in initial winMap
        for i in range(0, len(s1)): 
            winMap[s2[i]] = winMap.get(s2[i], 0) + 1 


        while end < len(s2): 
            if winMap == map1: 
                return True 
                
            else: 
                #slide window 
                winMap[s2[front]] -= 1 
                if winMap[s2[front]] == 0: 
                    del winMap[s2[front]]
                
                front += 1
                end += 1 

                if end < len(s2):
                    winMap[s2[end]] = winMap.get(s2[end], 0) + 1 
                


        return False 


        
        