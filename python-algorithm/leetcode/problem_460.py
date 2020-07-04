"""460. LFU Cache
https://leetcode.com/problems/lfu-cache/


Design and implement a data structure for Least Frequently Used (LFU) cache.
It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key
exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present.
When the cache reaches its capacity, it should invalidate the least frequently
used item before inserting a new item. For the purpose of this problem,
when there is a tie (i.e., two or more keys that have the same frequency),
the least recently used key would be evicted.

Note that the number of times an item is used is the number of calls to the get
and put functions for that item since it was inserted. This number is set to
zero when the item is removed.


Follow up:
Could you do both operations in O(1) time complexity?

Example:

LFUCache cache = new LFUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.get(3);       // returns 3.
cache.put(4, 4);    // evicts key 1.
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4
"""


class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.store = {}
        self.sorted_keys = []
        self.tree_map = {}

    def get(self, key: int) -> int:
        if key not in self.store:
            return -1
        self.sorted_keys.remove(key)
        self.sorted_keys.insert(0, key)
        self.tree_map[key] = self.tree_map[key] + 1
        self.tree_map = self._sort_by_value(self.tree_map)
        return self.store[key]

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        if key not in self.store:
            if len(self.store) == self.capacity:
                lfu_value = list(self.tree_map.values())[0]
                lfu_keys = []
                for k, v in self.tree_map.items():
                    if v == lfu_value:
                        lfu_keys.append(k)
                for k in reversed(self.sorted_keys):
                    if k in lfu_keys:
                        self.sorted_keys.remove(k)
                        self.sorted_keys.insert(0, key)
                        del self.store[k]
                        self.store[key] = value
                        del self.tree_map[k]
                        self.tree_map[key] = 0
                        break
            else:
                self.sorted_keys.insert(0, key)
                self.store[key] = value
                self.tree_map[key] = 0
        else:
            self.sorted_keys.remove(key)
            self.sorted_keys.insert(0, key)
            self.store[key] = value
            self.tree_map[key] = self.tree_map[key] + 1

        self.tree_map = self._sort_by_value(self.tree_map)

    def _sort_by_value(self, unsorted_map):
        return {k: v for k, v in
                sorted(unsorted_map.items(), key=lambda item: item[1])}


if __name__ == '__main__':
    # [[2], [1, 1], [2, 2], [1], [3, 3], [2], [3], [4, 4], [1], [3], [4]]
    cache = LFUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    print(cache.get(1) == 1)  # 1
    cache.put(3, 3)
    print(cache.get(2) == -1)  # -1
    print(cache.get(3) == 3)  # 3
    cache.put(4, 4)
    print(cache.get(1) == -1)  # -1
    print(cache.get(3) == 3)  # 3
    print(cache.get(4) == 4)  # 4

    # ["LFUCache","put","get"]
    # [[0],[0,0],[0]]
    cache1 = LFUCache(0)
    cache1.put(0, 0)
    print(cache1.get(0) == -1)
