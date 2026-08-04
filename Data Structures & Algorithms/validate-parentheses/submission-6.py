class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            '(': ')',
            '{':'}',
            '[':']'
        }
        
        stack = []

        for p in s: 
            if p not in pairs: 
                if not stack or pairs[stack.pop()] != p:
                    return False 
            else:
                stack.append(p)

        return len(stack) == 0