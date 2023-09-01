"""338. Counting Bits
https://leetcode.com/problems/counting-bits/
"""
from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n + 1)
        idx = 2
        for i in range(1, n + 1):
            if i == idx:
                idx *= 2
            ans[i] = ans[i - idx // 2] + 1
        return ans

    def count_bits_2(self, num: int) -> List[int]:
        ans = [0]
        step = 1
        while len(ans) < num + 1:
            n = min(step, num + 1 - len(ans))
            for i in range(n):
                ans.append(ans[i] + 1)
            step *= 2
        return ans
