class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += str(len(s)) + '#' + s
        return encoded

# 5#Hello5#World

    def decode(self, s: str) -> List[str]:
       
        decoded = []
        left = 0 #number finder

        while left < len(s):
            right = left  # hashtag finder
            while right < len(s) and s[right] != '#':
                right += 1
            

            wordLength = int(s[left:right])

            decoded.append(s[right + 1 : right + wordLength + 1])

            left = right + wordLength + 1
        
        return decoded
