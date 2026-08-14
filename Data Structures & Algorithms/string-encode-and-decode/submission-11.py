class Solution:

    def encode(self, strs: List[str]) -> str:
        #.   5#Ethan4#Chao

        encoded = ""
        for s in strs: 
            encoded += str(len(s)) + '#' + s
        return encoded


    def decode(self, s: str) -> List[str]:
        left = 0 #start of len delim
        right = 0 # hashtag finder
        decoded = []

        while left < len(s): 
            while s[right] != '#': 
                right += 1 

            delimLen = int(s[left:right])

            decoded.append(s[right+1 : right+delimLen+1])

            left = right + delimLen + 1 
            right = left
        
        return decoded



