"""380. Insert Delete GetRandom O(1)
https://leetcode.com/problems/insert-delete-getrandom-o1/
"""
import random


class RandomizedSet:

    def __init__(self):
        self.nums = list()
        self.store = dict()

    def insert(self, val: int) -> bool:
        if val in self.store:
            return False
        self.nums.append(val)
        self.store[val] = len(self.nums) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.store:
            return False
        i = self.store[val]
        self.nums[i] = self.nums[-1]
        self.nums.pop()
        del self.store[val]
        if i < len(self.nums):
            self.store[self.nums[i]] = i
        return True

    def getRandom(self) -> int:
        i = random.randint(0, len(self.nums) - 1)
        return self.nums[i]
