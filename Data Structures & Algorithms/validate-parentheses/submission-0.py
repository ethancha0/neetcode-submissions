class Solution:
    def isValid(self, s: str) -> bool:
        
        pairs = {
            '(':')',
            '[':']',
            '{':'}',
        }

        stack = []

        for elem in s: 
            if elem in pairs: 
                stack.append(elem)
            else:
                if len(stack) == 0 or pairs[stack[-1]] != elem:
                    return False
                else:
                    stack.pop() 
            
        
        return len(stack) == 0 
                    