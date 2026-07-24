class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tMap = {} 
        for elem in t: 
            tMap[elem] = tMap.get(elem, 0) + 1 
        
        winMap = {} 
        left = 0 
        ans = ""

        haveCount = 0
        needCount = len(tMap)

        for right in range(len(s)): 
            winMap[s[right]] = winMap.get(s[right], 0) + 1

            if s[right] in tMap and winMap[s[right]] == tMap[s[right]]:
                haveCount += 1 
            

            while haveCount == needCount: 
                if ans == "" or (right-left+1) < len(ans): 
                    ans = s[left:right+1]

                #shrink by moving left
                sub = s[left]
                winMap[sub] -= 1 
                left += 1

                #check if have still matches need count 
                if sub in tMap and tMap[sub] > winMap[sub]:
                    haveCount -= 1 
        return ans

                