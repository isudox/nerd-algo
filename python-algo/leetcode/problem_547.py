"""547. Number of Provinces
https://leetcode.com/problems/number-of-provinces/
"""
from typing import List


class Solution:
    def find_circle_num(self, is_connected: List[List[int]]) -> int:
        def dfs(row: int):
            visited[row] = True
            for col in range(n):
                if is_connected[row][col] == 1 and not visited[col]:
                    dfs(col)

        n = len(is_connected)
        num = 0
        visited = [False] * n
        for i in range(n):
            if not visited[i]:
                dfs(i)
                num += 1
        return num
