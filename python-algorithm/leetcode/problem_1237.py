"""1237. Find Positive Integer Solution for a Given Equation
https://leetcode.cn/problems/find-positive-integer-solution-for-a-given-equation/
"""
from typing import List


class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        ans = []
        for x in range(1, 1001):
            lo, hi = 1, 1000
            while lo <= hi:
                y = (lo + hi) // 2
                tmp = customfunction.f(x, y)
                if tmp == z:
                    ans.append([x, y])
                    break
                if tmp > z:
                    hi = y - 1
                else:
                    lo = y + 1
        return ans
