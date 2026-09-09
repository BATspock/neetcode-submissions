class MinStack:

    def __init__(self):
        self.stack = []
        self.monotonic_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        
        if len(self.monotonic_stack) > 0  and self.monotonic_stack[-1] >= val:
            self.monotonic_stack.append(val)
        elif len(self.monotonic_stack) ==0:
            self.monotonic_stack.append(val)

    def pop(self) -> None:

        val = self.stack.pop()

        if len(self.monotonic_stack) > 0 and self.monotonic_stack[-1] == val:
            self.monotonic_stack.pop()
        

    def top(self) -> int:
        
        return self.stack[-1]

    def getMin(self) -> int:
        
        return self.monotonic_stack[-1]