class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        # freq map 
        freq = {} 
        for elem in s1:
            if elem in freq: 
                freq[elem] += 1
            else: 
                freq[elem] = 1
        
        # fixed sliding window 
        left = 0 
        right = len(s1)-1


        # setup initial window 
        win = {} 
        for elem in s2[:len(s1)]:
            if elem in win:
                win[elem] += 1
            else:
                win[elem] = 1 
        

        while right < len(s2): 
            if win == freq: 
                return True
            else:
                win[s2[left]] -= 1 
                if win[s2[left]] == 0: 
                    del win[s2[left]]

                left += 1 
                right += 1

                if right < len(s2):
                    win[s2[right]] = win.get(s2[right], 0) + 1
        
        return False



            