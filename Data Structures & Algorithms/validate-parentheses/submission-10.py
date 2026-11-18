class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            '(':')',
            '{':'}',
            '[':']',
        }

        stack = [] 

        for elem in s:
            if len(stack) > 0 and elem == pairs[stack[-1]]:
                stack.pop() 
            else:
                if elem not in pairs: 
                    return False 
                stack.append(elem)

        if len(stack) > 0:
            return False
        return True