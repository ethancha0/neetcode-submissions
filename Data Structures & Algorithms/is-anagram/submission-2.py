class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        if len(s) != len(t):
            return False
        
        freqMap = {}
        for elem in s: 
            freqMap[elem] = freqMap.get(elem, 0) + 1 

        
        for elem in t: 
            if elem in freqMap: 
                freqMap[elem] -= 1

                if freqMap[elem] == 0:
                    del freqMap[elem]
            else: 
                return False 

        return len(freqMap) == 0 
