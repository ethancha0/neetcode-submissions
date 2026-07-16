class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False 

        # create freq map of s1
        map1 = {}
        for elem in s1: 
            map1[elem] = map1.get(elem, 0) + 1 

        # create initial fixed sliding window 
        map2 = {} 
        left = 0 
        right = len(s1)-1

        for i in range(len(s1)): 
            if s2[i] in map2:
                map2[s2[i]] += 1 
            else: 
                map2[s2[i]] = 1 



        while right < len(s2): 
            if map1 == map2: 
                return True 
            
            #move right ptr (only add) 
            right += 1
            if right < len(s2):
                map2[s2[right]] = map2.get(s2[right], 0) + 1
          

            #move left ptr (only sub)
            map2[s2[left]] -= 1 
            if map2[s2[left]] == 0: 
                del map2[s2[left]]

            left += 1 
        
        return False






        