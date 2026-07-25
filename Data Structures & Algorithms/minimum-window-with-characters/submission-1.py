class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tMap = {} 
        for elem in t: 
            tMap[elem] = tMap.get(elem, 0) + 1

        winMap = {} 
        left = 0 
        
        needCount = len(tMap) 
        haveCount = 0

        ans = ""


        for i in range(len(s)): 
            #build window map 
            winMap[s[i]] = winMap.get(s[i], 0) + 1
            #check counts equal
            if s[i] in tMap and winMap[s[i]] == tMap[s[i]]: 
                haveCount += 1

            while needCount == haveCount:
                if ans == "" or i-left+1 < len(ans):
                    ans = s[left:i+1] 
                removed = s[left]
                winMap[removed] -= 1 
                left += 1 

                if removed in tMap and winMap[removed] < tMap[removed]:
                    haveCount -= 1 

        return ans
