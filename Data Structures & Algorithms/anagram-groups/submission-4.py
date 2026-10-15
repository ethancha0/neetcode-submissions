class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        tmap = {}

        for s in strs:
            sortedWord = "".join(sorted(s))
            if sortedWord not in tmap:
                tmap[sortedWord] = []
            tmap[sortedWord].append(s)

        return list(tmap.values())
            