"""1656. Design an Ordered Stream
https://leetcode.com/problems/design-an-ordered-stream/
"""
from typing import List


class OrderedStream:

    def __init__(self, n: int):
        self.ptr = 1
        self.store = [''] * (n + 1)

    def insert(self, idKey: int, value: str) -> List[str]:
        self.store[idKey] = value
        ret = []
        if idKey != self.ptr:
            return []
        while idKey < len(self.store) and self.store[idKey]:
            ret.append(self.store[idKey])
            idKey += 1
        self.ptr = idKey
        return ret
