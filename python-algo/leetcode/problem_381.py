"""381. Insert Delete GetRandom O(1) - Duplicates allowed
https://leetcode.com/problems/insert-delete-getrandom-o1-duplicates-allowed/

Design a data structure that supports all following operations in average O(1) time.
Note: Duplicate elements are allowed.

    insert(val): Inserts an item val to the collection.
    remove(val): Removes an item val from the collection if present.
    getRandom: Returns a random element from current collection of elements.
    The probability of each element being returned is linearly related to
    the number of same value the collection contains.
"""
import random


class RandomizedCollection:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.arr = []
        self.size = 0
        self.index = {}

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """
        self.arr.append(val)
        self.size += 1
        if val in self.index:
            self.index[val].append(self.size - 1)
            return False
        else:
            self.index[val] = [self.size - 1]
            return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """
        if val not in self.index:
            return False
        pos = self.index[val].pop()
        if not self.index[val]:
            del self.index[val]
        if pos < self.size - 1:
            self.arr[pos] = self.arr[self.size - 1]
            self.index[self.arr[pos]].remove(self.size - 1)
            self.index[self.arr[pos]].append(pos)
        self.arr.pop()
        self.size -= 1
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """
        index = random.randint(0, self.size - 1)
        return self.arr[index]

# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
