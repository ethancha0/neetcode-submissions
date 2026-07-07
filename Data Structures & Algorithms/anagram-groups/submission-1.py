class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hash = {} 
        for elem in strs: 
            sort = "".join(sorted(elem))
            if sort in hash: 
                hash[sort].append(elem)
            else: 
                hash[sort] = [elem]

        return list(hash.values())