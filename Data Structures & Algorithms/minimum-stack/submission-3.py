class MinStack:

    def __init__(self):
        self.stack = []
        self.m = []

    def push(self, val: int) -> None:
        if not self.m or val <= self.m[-1]:
            self.m.append(val)

        self.stack.append(val)

    def pop(self) -> None:
        v = self.stack.pop()
        if self.m and v == self.m[-1]:
            self.m.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.m[-1]