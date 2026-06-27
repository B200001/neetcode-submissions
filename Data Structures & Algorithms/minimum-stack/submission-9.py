class MinStack:

    def __init__(self):
        self.first = []
        self.second = []

    def push(self, val: int) -> None:
        self.first.append(val)
        if not self.second:
            self.second.append(val)
            return
        self.second.append(min(val, self.second[-1]))

    def pop(self) -> None:
        self.first.pop()
        self.second.pop()

    def top(self) -> int:
        return self.first[-1]

    def getMin(self) -> int:
        if not self.second:
            return 
        return self.second[-1]
