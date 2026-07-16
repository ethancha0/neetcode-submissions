class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs: 
            encoded += str(len(s)) + '#' + s
        return encoded
        #     5#ethan4#chao


    def decode(self, s: str) -> List[str]:
        left = 0 
        right = 0 
        decoded = []

        while left < len(s):
            while s[right] != '#':
                right += 1 
            
            delimLen = int(s[left:right])

            decoded.append(s[right+1 : right+delimLen+1])

            left = right + delimLen + 1 
            right = left
        
        return decoded

