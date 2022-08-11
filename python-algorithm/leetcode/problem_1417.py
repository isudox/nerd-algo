"""1417. Reformat The String
https://leetcode.cn/problems/reformat-the-string/
"""
from typing import List


class Solution:
    def reformat(self, s: str) -> str:
        def mix(a: List[str], b: List[str]) -> str:
            if abs(len(a) - len(b)) > 1:
                return ''
            if len(a) < len(b):
                return mix(b, a)
            ret = ''
            for i in range(len(a)):
                ret += a[i]
                if i < len(b):
                    ret += b[i]
            return ret

        alpha = []
        nums = []
        for ch in s:
            if '0' <= ch <= '9':
                nums.append(ch)
            else:
                alpha.append(ch)
        return mix(alpha, nums)
