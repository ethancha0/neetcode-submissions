class Solution:
    #     5#ethan#4chao
    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for word in strs: 
            encoded += (str(len(word)) + '#' + word )

        return encoded



    def decode(self, s: str) -> List[str]:

        #left: wordLength finder, right: hashTag finder
        left = 0                    
        right = 0 

        ans = []
        while left < len(s):

            while right < len(s) and s[right] != '#':
                right += 1

            # get len delimiter
            length = int(s[left:right])

            ans.append(s[right+1 : right+length+1])
            left = right + length + 1
            right = left
        
        return ans

        