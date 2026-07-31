class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # (sortedword : word)
        hashMap = {} 

        for w in strs: 
            sortedWord = "".join(sorted(w))
            if sortedWord not in hashMap:
                hashMap[sortedWord] = [] 
            hashMap[sortedWord].append(w)

        return list(hashMap.values())