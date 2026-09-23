from collections import deque
class MinStack:
    def __init__(self):
        self.stack = []
        self.minstack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)

        current_min = val if not self.minstack else min(val, self.minstack[-1])
        self.minstack.append(current_min)

    def pop(self) -> None:
        self.stack.pop()
        self.minstack.pop()

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minstack[-1]


        
