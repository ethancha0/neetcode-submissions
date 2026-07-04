class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        operator = ['+', '-', '*', '/']
        stack = []


        for elem in tokens: 
            if elem not in operator: 
                stack.append(int(elem))
            else:
                o1 = stack.pop()
                o2 = stack.pop() 

                if elem == '+':
                    stack.append(o2 + o1)
                elif elem == '-':
                    stack.append(o2 - o1)
                elif elem == '*':
                    stack.append(o2 * o1)
                else: 
                    stack.append(int(o2/o1))
        
        return stack[-1]

