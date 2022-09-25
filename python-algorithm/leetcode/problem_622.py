"""622. Design Circular Queue
https://leetcode.com/problems/design-circular-queue/
"""


class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = [0] * k
        self.head = 0
        self.tail = -1
        self.size = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.tail = (self.tail + 1) % len(self.queue)
        self.queue[self.tail] = value
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.head = (self.head + 1) % len(self.queue)
        self.size -= 1
        return True

    def Front(self) -> int:
        return -1 if self.isEmpty() else self.queue[self.head]

    def Rear(self) -> int:
        return -1 if self.isEmpty() else self.queue[self.tail]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == len(self.queue)

