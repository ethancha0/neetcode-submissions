class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tMap = {} 
        for elem in t: 
            tMap[elem] = tMap.get(elem, 0) + 1 
        
        windowMap = {}
        left = 0 
        haveCount = 0 
        needCount = len(tMap)
        ans = ""

        for right in range(len(s)):
            windowMap[s[right]] = windowMap.get(s[right], 0) + 1 

            if s[right] in tMap and windowMap[s[right]] == tMap[s[right]]:
                haveCount += 1 
            
            while haveCount == needCount: 
                if ans == "" or right-left+1 < len(ans):
                    ans = s[left:right+1]
                #increment left 
                popped = s[left]
                left += 1 
                windowMap[popped] -= 1 

                #check if still match 
                if popped in tMap and windowMap[popped] < tMap[popped]: 
                    haveCount -= 1 
        
        return ans
