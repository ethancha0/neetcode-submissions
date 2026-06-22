class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        hashMap = {} 

        for elem in s: 
            if elem in hashMap:
                hashMap[elem] += 1
            else:
                hashMap[elem] = 1
        

        for elem in t:
            if elem in hashMap: 
                hashMap[elem] -= 1

                if hashMap[elem] == 0:
                    del hashMap[elem]

            else: 
                return False

        
        return len(hashMap) == 0 