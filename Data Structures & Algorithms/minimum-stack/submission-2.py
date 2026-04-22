class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        min_value = self.min_stack[-1] if len(self.min_stack) else val
        if val < min_value:
            min_value = val

        self.min_stack.append(min_value)
        

    def pop(self) -> None:
        if len(self.stack):
            last_el = self.stack.pop()
            self.min_stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min_stack[-1]
        
