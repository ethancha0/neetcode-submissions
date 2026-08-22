class MyQueue:

    def __init__(self):
        self.stack1 = [] #normal 
        self.stack2 = [] #reversed?
        

    def push(self, x: int) -> None:
        self.stack1.append(x)
        

    def pop(self) -> int:
        #move all elems from s1 to s2, except last one
        if len(self.stack2) == 0:
            while len(self.stack1) > 0: 
                self.stack2.append(self.stack1.pop())
        
        return self.stack2.pop()


        

    def peek(self) -> int:
        if len(self.stack2) == 0: 
            while len(self.stack1) > 0: 
                self.stack2.append(self.stack1.pop())
        
        return self.stack2[-1]
        

    def empty(self) -> bool:
        return len(self.stack1) == 0 and len(self.stack2) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()


# ex: stack1 = [1, 2, 3], we pop, putting everything into s2, reversing the stack
#     stack2 = [3, 2, 1]


#note: a queue (FIFO) is just opposite of a stack (FILO)
#could use deque (able to push/pop both ways )