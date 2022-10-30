"""
https://leetcode.com/problems/letter-case-permutation/
"""
from typing import List


class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        def dfs(i: int) -> List[str]:
            if i == len(s):
                return ['']
            ret = []
            nxt = dfs(i + 1)
            for comb in nxt:
                ret.append(s[i] + comb)
            d = ord(s[i])
            if 65 <= d <= 90:
                nxt = dfs(i + 1)
                for comb in nxt:
                    ret.append(chr(d + 32) + comb)
            elif 97 <= d <= 122:
                nxt = dfs(i + 1)
                for comb in nxt:
                    ret.append(chr(d - 32) + comb)
            return ret

        return dfs(0)
