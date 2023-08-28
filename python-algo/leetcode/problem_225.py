"""225. Implement Stack using Queues
"""


class MyStack:

    def __init__(self):
        self.q = [[], []]
        self.i = 0

    def push(self, x: int) -> None:
        self.q[self.i].append(x)

    def pop(self) -> int:
        while len(self.q[self.i]) > 1:
            num = self.q[self.i].pop(0)
            self.q[1 - self.i].append(num)
        ret = self.q[self.i].pop()
        self.i = 1 - self.i
        return ret

    def top(self) -> int:
        return self.q[self.i][-1]

    def empty(self) -> bool:
        return len(self.q[self.i]) == 0

