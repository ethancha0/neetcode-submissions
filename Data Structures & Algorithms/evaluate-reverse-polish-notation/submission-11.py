class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = [] 
        operator = ['+', '-', '*', '/']
        for elem in tokens: 
            if elem not in operator: 
                stack.append(elem)
            
            else:
                a = int(stack.pop())
                b = int(stack.pop())

                if elem == '+':
                    stack.append(b + a)
                elif elem == '-':
                    stack.append(b - a)
                elif elem == '*':
                    stack.append(b * a)
                else: 
                    stack.append(int(b / a))
            
        return int(stack[-1])

        