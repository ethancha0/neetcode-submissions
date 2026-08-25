class Solution:
    def longestPalindrome(self, s: str) -> int:
        # freqMap, if two letters, add 1 to count

        count = 0 
        freqMap = {}
        for elem in s: 
            freqMap[elem] = freqMap.get(elem, 0) + 1 
            if freqMap[elem] == 2: 
                freqMap[elem] = 0
                count +=2
        
        #account for odds 
        for elem in s: 
            if freqMap[elem] == 1:
                count += 1 
                break

        return count