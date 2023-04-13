"""688. Knight Probability in Chessboard
https://leetcode.com/problems/knight-probability-in-chessboard/
"""
import functools


def knight_probability(self, n: int, k: int, row: int, column: int) -> float:
    @functools.lru_cache(None)
    def dfs(x: int, y: int, steps: int) -> int:
        if steps == 0:
            if 0 <= x < n and 0 <= y < n:
                return 1
        ret = 0
        for nx, ny in [[x + 1, y + 2], [x + 1, y - 2], [x - 1, y + 2], [x - 1, y - 2],
                       [x - 2, y + 1], [x - 2, y - 1], [x + 2, y + 1], [x + 2, y - 1]]:
            if 0 <= nx < n and 0 <= ny < n:
                ret += dfs(nx, ny, steps - 1)
        return ret

    return dfs(row, column, k) / (8 ** k)
