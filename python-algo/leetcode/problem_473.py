"""473. Matchsticks to Square
https://leetcode.com/problems/matchsticks-to-square/
"""
from typing import List


class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        totalLen = sum(matchsticks)
        if totalLen % 4:
            return False
        matchsticks.sort(reverse=True)

        edges = [0] * 4

        def dfs(idx: int) -> bool:
            if idx == len(matchsticks):
                return True
            for i in range(4):
                edges[i] += matchsticks[idx]
                if edges[i] <= totalLen // 4 and dfs(idx + 1):
                    return True
                edges[i] -= matchsticks[idx]
            return False

        return dfs(0)

