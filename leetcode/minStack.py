class MinStack:

    def __init__(self): #this is a constructor method in python
        self.stack = [] #this is the og stack
        self.minStack = [] #this is the stack that tracks the minumum value

    def push(self, val: int) -> None:
        self.stack.append(val) #adding the new value
        if self.stack: #if the self stack is not empty, get the minumum value and add that to the minStack
            val = min(val, self.minStack[-1])
        self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop() #popping the most recent element
        self.minStack.pop()

    def top(self) -> int: #peeking the most recent element
        return self.stack[-1]
        
    def getMin(self) -> int:
        return self.minStack[-1] #getting the top value at minumum value 
