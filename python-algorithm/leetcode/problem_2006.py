"""2006. Count Number of Pairs With Absolute Difference K
https://leetcode.com/problems/count-number-of-pairs-with-absolute-difference-k/
"""
import collections
from typing import List


def count_k_difference(nums: List[int], k: int) -> int:
    ans = 0
    store = collections.Counter()
    for num in nums:
        ans += store[num + k]
        if k != 0:
            ans += store[num - k]
        store[num] += 1
    return ans
