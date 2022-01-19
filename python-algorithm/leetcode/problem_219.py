"""219. Contains Duplicate II
https://leetcode.com/problems/contains-duplicate-ii/
"""
import collections
from typing import List


def contains_nearby_duplicate(nums: List[int], k: int) -> bool:
    store = collections.defaultdict(int)
    for i, num in enumerate(nums):
        if num in store and i - store[num] <= k:
            return True
        store[num] = i
    return False
