"""1659. Maximize Grid Happiness
https://leetcode.com/problems/maximize-grid-happiness/
"""
import functools


class Solution:
    def getMaxGridHappiness(self, m: int, n: int, introvertsCount: int, extrovertsCount: int) -> int:
        @functools.cache
        def dfs(pos: int, mask: int, iv: int, ev:int) -> int:
            if pos == m * n or (iv == 0 and ev == 0):
                return 0
            res = 0
            up, left = mask // p[n - 1], mask % 3
            if pos % n == 0:
                left = 0
            for i in range(3):
                if (i == 1 and iv == 0) or (i == 2 and ev == 0):
                    continue
                next_mask = mask % p[n - 1] * 3 + i
                score_sum = dfs(pos + 1, next_mask, iv - (i == 1), ev - (i == 2)) + score[up][i] + score[left][i]
                if i == 1:
                    score_sum += 120
                elif i == 2:
                    score_sum += 40
                res = max(res, score_sum)
            return res

        score = [
            [0, 0, 0],
            [0, -60, -10],
            [0, -10, 40]
        ]
        p = [1]
        for _ in range(1, n):
            p.append(p[-1] * 3)
        return dfs(0, 0, introvertsCount, extrovertsCount)
