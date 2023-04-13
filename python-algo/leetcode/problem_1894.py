"""1894. Find the Student that Will Replace the Chalk
https://leetcode.com/problems/find-the-student-that-will-replace-the-chalk/
"""
from typing import List


class Solution:
    def chalk_replacer(self, chalk: List[int], k: int) -> int:
        i, n = 0, len(chalk)
        k %= sum(chalk)
        while chalk[i] <= k:
            k -= chalk[i]
            i += 1
            if i == n:
                i = 0
        return i
