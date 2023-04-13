"""1306. Jump Game III
https://leetcode.com/problems/jump-game-iii/
"""
from typing import List


class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        def dfs(i: int):
            nonlocal ans
            if ans:
                return
            if i < 0 or i >= len(arr):
                return
            if visited[i]:
                return
            visited[i] = True
            if arr[i] == 0:
                ans = True
                return
            dfs(i + arr[i])
            dfs(i - arr[i])

        ans = False
        visited = [False] * len(arr)
        dfs(start)
        return ans
