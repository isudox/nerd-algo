"""460. LFU Cache
https://leetcode.com/problems/lfu-cache/
Follow up: Could you do both operations in O(1) time complexity?
"""


class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.counter = dict()
        self.timestamp = 0
        self.store = dict()

    def get(self, key: int) -> int:
        if key not in self.store:
            return -1
        self.timestamp += 1
        self.counter[key][0] += 1
        self.counter[key][1] = self.timestamp
        return self.store[key]

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        if key not in self.store and len(self.store) == self.capacity:
            lfu_key, lfu_cnt, lfu_ts = None, 100000, 100000
            for k, cnt in self.counter.items():
                if cnt[0] < lfu_cnt or cnt[0] == lfu_cnt and cnt[1] < lfu_ts:
                    lfu_cnt = cnt[0]
                    lfu_ts = cnt[1]
                    lfu_key = k
            del self.counter[lfu_key]
            del self.store[lfu_key]
        self.timestamp += 1
        self.counter[key] = [(self.counter[key][0] if key in self.store else 0) + 1, self.timestamp]
        self.store[key] = value
