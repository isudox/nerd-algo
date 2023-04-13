from functools import lru_cache


class Solution:
    def num_distinct(self, s: str, t: str) -> int:
        @lru_cache(None)
        def dfs(x: int, y: int) -> int:
            if y == len(t):
                return 1
            if x == len(s):
                return 0
            ret = dfs(x + 1, y)
            if s[x] == t[y]:
                ret += dfs(x + 1, y + 1)
            return ret

        return dfs(0, 0)
