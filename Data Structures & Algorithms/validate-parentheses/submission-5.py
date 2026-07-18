class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            '(':')',
            '[':']',
            '{':'}'
        }

        stack = []

        for p in s:
            if p in pairs: 
                stack.append(p)
            else:
                if len(stack) <= 0 or p != pairs[stack[-1]]:
                    return False
                else: 
                    stack.pop()
        
        return len(stack) == 0
