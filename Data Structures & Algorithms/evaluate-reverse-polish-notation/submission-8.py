class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        # if two numbers, pop 
        # if one number, operate on total 

        stack = [] 

        for elem in tokens:

            if elem == "+":
                stack.append(stack.pop() + stack.pop())
            elif elem == "-":
                b, a = stack.pop(), stack.pop()
                stack.append(a - b)
            elif elem == "*":
                stack.append(stack.pop() * stack.pop())
            elif elem == "/":
                b, a = stack.pop(), stack.pop()
                stack.append(int(float(a) / b))
            else:
                stack.append(int(elem))
        
        return stack[-1]
