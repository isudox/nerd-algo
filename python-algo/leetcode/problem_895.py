"""895. Maximum Frequency Stack
https://leetcode.com/problems/maximum-frequency-stack/
"""
import collections


class FreqStack:

    def __init__(self):
        self.stack = []
        self.counter = collections.Counter()
        self.mapper = collections.defaultdict(list)  # cnt -> vals
        self.max_cnt = 0

    def push(self, val: int) -> None:
        self.stack.append(val)
        old_cnt = self.counter[val]
        self.counter[val] += 1
        new_cnt = old_cnt + 1
        self.mapper[new_cnt].append(val)
        if new_cnt > self.max_cnt:
            self.max_cnt = new_cnt

    def pop(self) -> int:
        val = self.mapper[self.max_cnt].pop()
        self.counter[val] -= 1
        if not self.mapper[self.max_cnt]:
            max_cnt = 0
            for k, v in self.mapper.items():
                if v and k > max_cnt:
                    max_cnt = k
            self.max_cnt = max_cnt
        return val
