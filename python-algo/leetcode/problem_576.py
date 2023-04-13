"""576. Out of Boundary Paths
https://leetcode.com/problems/out-of-boundary-paths/
"""
from functools import lru_cache


class Solution:
    def find_paths(self, m: int, n: int, max_move: int, row: int, col: int) -> int:
        @lru_cache(None)
        def dfs(x: int, y: int, moves: int) -> int:
            if moves == 0:
                return 0
            if m - x > moves and x + 1 > moves and n - y > moves and y + 1 > moves:
                return 0
            ret = 0
            for d in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                nx, ny = x + d[0], y + d[1]
                if 0 <= nx < m and 0 <= ny < n:
                    ret += dfs(nx, ny, moves - 1) % 1000000007
                else:
                    ret += 1
            return ret % 1000000007

        return dfs(row, col, max_move)
