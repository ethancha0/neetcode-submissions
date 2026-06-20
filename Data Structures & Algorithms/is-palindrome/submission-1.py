class Solution:
    def isPalindrome(self, s: str) -> bool:

        front = 0 
        end = len(s) - 1

        while front < end: 
            while s[front].isalnum() == False and front < end:
                front += 1 
            while s[end].isalnum() == False and front < end:
                end -=1 

            if s[front].lower() != s[end].lower():
                return False

            front += 1
            end -=1 


        return True
        