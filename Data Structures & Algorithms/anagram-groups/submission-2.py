class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freqMap = {}

        for elem in strs:
            sortedWord = "".join(sorted(elem))
            if sortedWord in freqMap: 
                freqMap[sortedWord].append(elem)
            else: 
                freqMap[sortedWord] = [elem]

        return list(freqMap.values())