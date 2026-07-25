class MinStack:

    def __init__(self):
        self.stack = [] 
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        #only push to minstack if smaller than min or first 
        if len(self.minStack) == 0 or val < self.minStack[-1]:
            self.minStack.append(val)
        else: 
            self.minStack.append(self.minStack[-1])

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
        if self.minStack:
            self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        if len(self.minStack) > 0: 
            return self.minStack[-1]
        return 0