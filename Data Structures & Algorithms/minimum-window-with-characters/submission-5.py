class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #verify if t is a subset, then close in 
        tMap = {} #freqMap 
        for elem in t: 
            tMap[elem] = tMap.get(elem, 0) + 1 
        
        needCount = len(tMap)
        haveCount = 0

        ans = ""
        left = 0
        winMap = {}
        for i in range(len(s)): 
            winMap[s[i]] = winMap.get(s[i], 0) + 1 
            #check counts 
            if s[i] in tMap and winMap[s[i]] == tMap[s[i]]:
                haveCount += 1 
            
            while haveCount == needCount: 
                if ans == "" or i-left+1 < len(ans):
                    ans = s[left:i+1]
                
                #move left ptr
                temp = s[left]
                if temp in tMap and winMap[temp]-1 < tMap[temp]:
                    haveCount -= 1 

                winMap[temp] -= 1 
                left += 1 


        return ans