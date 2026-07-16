class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs: 
            encoded += str(len(s)) + '#' + s

        return encoded

        #      5#ethan4#chao

    def decode(self, s: str) -> List[str]:
        left = 0 #finds length
        right = 0 #finds hashtags

        decoded = []

        while left < len(s):   #. check on this 

            while right < len(s) and s[right] != '#':
                right += 1 

            lengthDelim = int(s[left:right])

            decoded.append(s[right+1 : right+lengthDelim+1])

            left = right+lengthDelim+1
            right = left

        
        return decoded
            


