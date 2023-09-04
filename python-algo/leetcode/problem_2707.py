"""2707. Extra Characters in a String
https://leetcode.com/problems/extra-characters-in-a-string/
"""
from typing import List
from functools import cache


class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        @cache
        def dfs(pre: str, i: int) -> int:
            if i == len(s):
                if not pre or pre in d:
                    return 0
                return len(pre)
            cur = pre + s[i]
            ret = dfs(cur, i + 1)
            if cur in d:
                ret = min(ret, dfs('', i + 1))
            else:
                ret = min(ret, dfs(s[i], i + 1) + len(pre), dfs('', i + 1) + len(cur))
            return ret

        d = set(dictionary)
        return dfs('', 0)