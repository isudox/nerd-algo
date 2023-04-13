"""532. K-diff Pairs in an Array
https://leetcode.com/problems/k-diff-pairs-in-an-array/
"""
import collections
from typing import List


def find_pairs(nums: List[int], k: int) -> int:
    ans = 0
    if k == 0:
        counter = collections.Counter(nums)
        for cnt in counter.values():
            if cnt > 1:
                ans += 1
        return ans
    store = set()
    for num in nums:
        a, b = num + k, num - k
        if a in store and num not in store:
            ans += 1
        if a != b and b in store and num not in store:
            ans += 1
        store.add(num)
    return ans
