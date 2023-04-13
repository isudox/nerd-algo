"""677. Map Sum Pairs
https://leetcode.com/problems/map-sum-pairs/
"""


class MapSum:

    def __init__(self):
        self.store = dict()

    def insert(self, key: str, val: int) -> None:
        self.store[key] = val

    def sum(self, prefix: str) -> int:
        ret = 0
        for k, v in self.store.items():
            if k.startswith(prefix):
                ret += v
        return ret
