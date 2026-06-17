class MinStack:

    def __init__(self):
        self.first = []              # main stack
        self.second = []             # min stack

    def push(self, val: int) -> None:
        self.first.append(val)
        if not self.second:
            self.second.append(val)  # ✅ first element always goes in
        else:
            self.second.append(min(val, self.second[-1]))  # ✅ track running min

    def pop(self) -> None:
        self.first.pop()             # ✅ always pop both together
        self.second.pop()            # ✅ keep them in sync

    def top(self) -> int:
        return self.first[-1]        # ✅ top of main stack

    def getMin(self) -> int:
        return self.second[-1]       # ✅ top of min stack = current minimum