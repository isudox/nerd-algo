"""1765. Map of Highest Peak
https://leetcode.com/problems/map-of-highest-peak/
"""
from typing import List


class Solution:
    def highest_peak(self, is_water: List[List[int]]) -> List[List[int]]:
        m, n = len(is_water), len(is_water[0])
        ans = [[-1] * n for _ in range(m)]
        q = []
        for i in range(m):
            for j in range(n):
                if is_water[i][j]:
                    ans[i][j] = 0
                    q.append([i, j])
        while q:
            i, j = q.pop(0)
            for x, y in [[i - 1, j], [i + 1, j], [i, j - 1], [i, j + 1]]:
                if 0 <= x < m and 0 <= y < n and ans[x][y] == -1:
                    ans[x][y] = ans[i][j] + 1
                    q.append([x, y])
        return ans
