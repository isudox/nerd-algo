"""80. Remove Duplicates from Sorted Array II
https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/
"""
import collections
from typing import List


def remove_duplicates(nums: List[int]) -> int:
    counter = collections.Counter()
    store = []
    for num in nums:
        if counter[num] < 2:
            counter[num] += 1
        if not store or store[-1] < num:
            store.append(num)
    i = 0
    for num in store:
        cnt = counter[num]
        for _ in range(cnt):
            nums[i] = num
            i += 1
    return i
