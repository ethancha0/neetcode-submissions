class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        # if two numbers, pop 
        # if one number, operate on total 

        operator = ['+', '-', '*', '/']
        stack = [] 

        for elem in tokens:
            if elem not in operator: 
                stack.append(int(elem))
            else:

                operand1 = stack.pop() 
                operand2 = stack.pop() 

                if elem == "+":
                    stack.append(operand1 + operand2)
                if elem == "-":
                    stack.append(operand2 - operand1)
                if elem == "*":
                    stack.append(operand1 * operand2)
                if elem == "/":
                    stack.append(int(operand2 / operand1))
        
        return stack[-1]
        