class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        operator = ['+', '-', '*', '/']

        stack = []

        for t in tokens: 
            if t not in operator: 
                stack.append(t)
            else: 
                o1 = int(stack.pop())
                o2 = int(stack.pop())

                if t == '+':
                    stack.append(o2 + o1)
                elif t == '-':
                    stack.append(o2 - o1)
                elif t == '*': 
                    stack.append(o2 * o1)
                else:
                    stack.append(int(o2 / o1))

        return int(stack[-1])
