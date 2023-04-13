"""432. All O`one Data Structure
https://leetcode.com/problems/all-oone-data-structure/
"""
import collections


class AllOne:

    def __init__(self):
        self.counter = collections.Counter()
        self.max_cnt = 0
        self.min_cnt = 0
        self.max_keys = []
        self.min_keys = []

    def inc(self, key: str) -> None:
        if self.counter[key] == self.min_cnt and self.counter[key] > 0:
            self.min_keys.remove(key)
        self.counter[key] += 1
        if self.counter[key] > self.max_cnt:
            self.max_cnt = self.counter[key]
            self.max_keys = [key]
        elif self.counter[key] == self.max_cnt:
            self.max_keys.append(key)

    def dec(self, key: str) -> None:
        if self.counter[key] == self.max_cnt:
            if len(self.max_keys) > 1:
                self.max_keys.remove(key)
            else:
                max_cnt = 0
                max_keys = []
                for k, cnt in self.counter.items():
                    if k == key:
                        continue
                    if cnt == max_cnt:
                        max_keys.append(k)
                    elif cnt > max_cnt:
                        max_cnt = cnt
                        max_keys = [k]
                self.max_cnt = max_cnt
                self.max_keys = max_keys
        elif


    def getMaxKey(self) -> str:
        return self.max_keys[0] if self.max_keys else ''

    def getMinKey(self) -> str:
        return self.min_keys[0] if self.min_keys else ''
