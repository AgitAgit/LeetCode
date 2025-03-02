# Tracker for the min value?
# It's not a min-heap, but a stack. Thats probably the catch.
# if it's a stack, that means I can't take elements from the middle?
# Ah, it doesn't say to POP the minimum element, only to retrieve it.
# after the initial finding of the minimum value, I can just check once
# when pushing/popping an element if it is smaller than the former min,
# and if it was the former min.

class MinStack:

    def __init__(self):
        self.min_val = None
        self.stack = []
        self.min_val_count = {}
        self.min_val_history = []

    def push(self, val: int) -> None:
        # if self.min_val is None:
        if len(self.stack) == 0:
            self.min_val = val
            self.min_val_history = [val]
        elif val <= self.min_val:
            self.min_val = val
            self.min_val_history.append(val)
        self.stack.append(val)

    def pop(self) -> None:
        if len(self.stack) > 0:
            popped = self.stack.pop()
            if popped == self.min_val:
                self.min_val_history.pop()
                if len(self.min_val_history) > 0:
                    self.min_val = self.min_val_history[-1]

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_val


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()