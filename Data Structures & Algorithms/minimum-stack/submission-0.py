class MinStack:

    def __init__(self):
        self.stack = []
        self.extra = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.extra:
            self.extra.append(min(self.extra[-1],val))
        else:
            self.extra.append(val)

    def pop(self) -> None:
        self.extra.pop()
        return self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.extra[-1]
        
