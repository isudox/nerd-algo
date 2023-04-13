"""174. Dungeon Game
https://leetcode.com/problems/dungeon-game/
"""
from typing import List
import sys


class Solution:
    def calculate_minimum_hp(self, dungeon: List[List[int]]) -> int:
        rows, cols = len(dungeon), len(dungeon[0])
        # dp[i][j] means the least hp from dungeon[i][j] to dungeon[-1][-1]
        dp = [[sys.maxsize] * cols for _ in range(rows)]
        dp[-1][-1] = (1 - dungeon[-1][-1]) if dungeon[-1][-1] < 0 else 1
        for i in range(rows - 1, -1, -1):
            for j in range(cols - 1, -1, -1):
                if i == rows - 1 and j == cols - 1:
                    continue
                if i < rows - 1:
                    # dp[i][j] = dp[i+1][j] - dungeon[i][j]
                    if dp[i + 1][j] - dungeon[i][j] > 0:
                        temp = dp[i + 1][j] - dungeon[i][j]
                    else:
                        temp = 1
                    dp[i][j] = min(dp[i][j], temp)
                if j < cols - 1:
                    # dp[i][j] = dp[i][j+1] - dungeon[i][j]
                    if dp[i][j + 1] - dungeon[i][j] > 0:
                        temp = dp[i][j+1] - dungeon[i][j]
                    else:
                        temp = 1
                    dp[i][j] = min(dp[i][j], temp)
        return dp[0][0]
