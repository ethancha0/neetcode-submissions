class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        #when integer, push to stack
        #when operator, pop last two and append new value 

        operator = ["+","-","*","/"]

        stack = [] 
        for t in tokens: 
            if t not in operator: 
                stack.append(int(t))
            else: 
                o1 = stack.pop() 
                o2 = stack.pop() 
                if t == "+": 
                    stack.append(o2 + o1)
                elif t == '-':
                    stack.append(o2 - o1)
                elif t == '*':
                    stack.append(o2 * o1)
                else: 
                    stack.append(int(o2 / o1))

        return stack[-1]