"""874. Walking Robot Simulation
https://leetcode.com/problems/walking-robot-simulation/
"""
from typing import List


class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        ans = 0
        x = y = di = 0
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        obs = set()
        for a, b in obstacles:
            obs.add((a, b))
        for c in commands:
            if c == -2:
                di = (di - 1) % 4
            elif c == -1:
                di = (di + 1) % 4
            else:
                for i in range(c):
                    if (x + dx[di], y + dy[di]) not in obs:
                        x += dx[di]
                        y += dy[di]
                        ans = max(ans, x * x + y * y)
        return ans
