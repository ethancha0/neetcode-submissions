class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # key => sortedWord, actualWord
        hashMap = {} 


        for elem in strs: 
            sortedWord = "".join(sorted(elem))

            if sortedWord in hashMap:
                hashMap[sortedWord].append(elem)
            else: 
                hashMap[sortedWord] = [elem]

        return list(hashMap.values())