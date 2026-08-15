class Solution:
    def isValid(self, s: str) -> bool:

        pairs = {
            '(': ')',
            '{' : '}',
            '[' : ']'
        }

        # if opening, always append 
        # if closing, check top for matching 

        stack = [] 

        for p in s: 
            if p in pairs:
                stack.append(p)
            else: 
                #closing
                if stack and pairs[stack[-1]] == p: 
                    stack.pop() 
                else: 
                    return False 

        return len(stack) == 0

        