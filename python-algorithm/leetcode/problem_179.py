"""179. Largest Number
https://leetcode.com/problems/largest-number/
"""
import functools
from typing import List


class Solution:
    def largest_number(self, nums: List[int]) -> str:
        arr = [str(num) for num in nums]
        store = [[] for _ in range(10)]
        for num in arr:
            store[int(num[0])].append(num)
        ans = ''
        for i in range(9, -1, -1):
            if not store[i]:
                continue
            store[i].sort(key=functools.cmp_to_key(
                lambda x, y: 1 if str(x) + str(y) < str(y) + str(x) else -1))
            ans += ''.join(store[i])
        i = 0
        while i < len(ans) and ans[i] == '0':
            i += 1
        return ans[i:] if i < len(ans) else '0'
