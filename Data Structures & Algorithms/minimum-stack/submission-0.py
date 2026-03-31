class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        min_so_far = self.min_stack[-1] if len(self.min_stack)!=0 else 1e10
        if val < min_so_far:
            self.min_stack.append(val)
        else:
            self.min_stack.append(min_so_far)
        

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min_stack[-1]
        
