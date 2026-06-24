class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
      
        numStack = [] 
        operator = ['+', '-', '/', '*']


        for elem in tokens:
            if elem not in operator: 
                numStack.append(int(elem))
            else:
                
                a = numStack.pop() 
                b = numStack.pop() 

                if elem == '+':
                    numStack.append(a + b)
                elif elem == '-':
                    numStack.append(b - a)
                elif elem == '*':
                    numStack.append(a * b)
                else:
                    numStack.append(int(b / a))
            
        return numStack[-1]
