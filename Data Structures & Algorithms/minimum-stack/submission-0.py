class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minStack and val < self.stack[self.minStack[len(self.minStack) - 1]]:
            self.minStack.append(len(self.stack) - 1)
        elif not self.minStack:
            self.minStack.append(len(self.stack) - 1)
        
    def pop(self) -> None:
        if self.minStack[len(self.minStack) - 1] == len(self.stack) - 1:
            self.minStack.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[len(self.stack) - 1]

    def getMin(self) -> int:
        return self.stack[self.minStack[len(self.minStack) - 1]]
