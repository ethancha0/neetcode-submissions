class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        if x < 0:
            return False 

        tempNum = ""

        strx = str(x)
        
        for i in range(len(strx)-1, -1, -1):
            tempNum += strx[i]

        return int(tempNum) == x
        
            