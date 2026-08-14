class Solution:
#  5#Ethan4#Chao
    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs: 
            encoded += str(len(s)) + '#' + s

        return encoded

#  5#Ethan4#Chao
    def decode(self, s: str) -> List[str]:
        decoded = [] 

        left = 0 # holds word len
        right = 0 # holds '#'

        while left < len(s):
            #find first #
            while s[right] != '#':
                right += 1 
            
            #calc first len
            delimLen = int(s[left:right])


            decoded.append(s[right+1 : right+delimLen+1])

            #move
            left = right + delimLen + 1
            right = left
            

        return decoded


