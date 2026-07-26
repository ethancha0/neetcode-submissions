class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tMap = {} 
        for elem in t:
            tMap[elem] = tMap.get(elem, 0) + 1 
        
        winMap = {}
        haveCount = 0 
        needCount = len(tMap)
        ans = ""
        left = 0

        for i in range(len(s)):
            winMap[s[i]] = winMap.get(s[i], 0) + 1 
            #check if freqs match 
            if s[i] in tMap and winMap[s[i]] == tMap[s[i]]:
                haveCount += 1

            #move left ptr while t still subset of s
            while haveCount == needCount:
                if ans == "" or (i-left+1) < len(ans):
                    ans = s[left:i+1]

                popped = s[left]
                winMap[s[left]] -= 1 
                
                left += 1 

                #check 
                if popped in tMap and winMap[popped] < tMap[popped]:
                    haveCount -= 1 

        return ans  

