"""735. Asteroid Collision
https://leetcode.com/problems/asteroid-collision/
"""
from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            keep = True
            while keep and stack and stack[-1] > 0 and a < 0:
                b = stack[-1]
                if abs(a) >= b:
                    stack.pop(-1)
                if abs(a) <= b:
                    keep = False
            if keep:
                stack.append(a)
        return stack
