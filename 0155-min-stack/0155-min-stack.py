import sys

class MinStack:

    def __init__(self):
        self.stack = []
        self.minimum = sys.maxsize
        
    def push(self, val: int) -> None:
        self.stack.append(val)
        if val < self.minimum:
            self.minimum = val

    def pop(self) -> None:
        if self.stack:
            removed = self.stack.pop()
            if removed == self.minimum:
                # Recalculate the minimum since the current minimum was removed
                self.minimum = min(self.stack, default=sys.maxsize)

    def top(self) -> int:
        return self.stack[-1] if self.stack else None

    def getMin(self) -> int:
        return self.minimum if self.stack else None


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
