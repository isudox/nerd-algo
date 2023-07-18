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


class LRUCache1:
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


class LRUCache2:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.keys = []
        self.map = {}

    def get(self, key: int) -> int:
        if key not in self.keys:
            return -1
        self._visit(key)
        return self.map[key]

    def put(self, key: int, value: int) -> None:
        if key not in self.map:
            if len(self.keys) == self.capacity:
                self._evict()
        self.map[key] = value
        self._visit(key)

    def _evict(self) -> None:
        evicted_key = self.keys[0]
        del self.map[evicted_key]
        self.keys = self.keys[1:]

    def _visit(self, key: int) -> None:
        if key in self.keys:
            self.keys.remove(key)
        self.keys.append(key)


class LinkedMap:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache3:

    def __init__(self, capacity):
        self.capacity = capacity
        self.map = {}
        self.head = LinkedMap(0, -1)
        self.tail = LinkedMap(0, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        if key not in self.map:
            return -1
        target = self.map[key]
        self._del(target)
        self._add(target)
        return target.value

    def put(self, key, value):
        if key not in self.map:
            if len(self.map) == self.capacity:
                del self.map[self.head.next.key]
                self._del(self.head.next)
        else:
            self._del(self.map[key])
        target = LinkedMap(key, value)
        self._add(target)
        self.map[key] = target

    def _del(self, node):
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p

    def _add(self, node):
        p = self.tail.prev
        p.next = node
        self.tail.prev = node
        node.prev = p
        node.next = self.tail
