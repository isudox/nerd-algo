"""146. LRU Cache
https://leetcode.com/problems/lru-cache/

Design and implement a data structure for Least Recently Used (LRU) cache.
It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key
exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present.
When the cache reached its capacity, it should invalidate the least recently
used item before inserting a new item.

The cache is initialized with a positive capacity.

Follow up:
Could you do both operations in O(1) time complexity?


Example:

LRUCache cache = new LRUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4
"""


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = {}
        self.sorted_keys = []

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        self.sorted_keys.remove(key)
        self.sorted_keys.insert(0, key)
        return self.map[key]

    def put(self, key: int, value: int) -> None:
        if key not in self.map:
            if len(self.map) == self.capacity:
                lru_key = self.sorted_keys[-1]
                self.sorted_keys.remove(lru_key)
                self.sorted_keys.insert(0, key)
                del self.map[lru_key]
                self.map[key] = value
            else:
                self.sorted_keys.insert(0, key)
                self.map[key] = value
        else:
            self.sorted_keys.remove(key)
            self.sorted_keys.insert(0, key)
            self.map[key] = value


if __name__ == "__main__":
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    print(cache.get(1))
    cache.put(3, 3)
    print(cache.get(2))
    print(cache.get(3))
