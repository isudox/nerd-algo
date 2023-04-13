"""682. Baseball Game
https://leetcode.com/problems/baseball-game/
"""
from typing import List


class Solution:
    def calPoints(self, ops: List[str]) -> int:
        q = []
        neg = False
        for op in ops:
            if op == '+':
                q.append(q[-1] + q[-2])
            elif op == 'D':
                q.append(q[-1] * 2)
            elif op == 'C':
                q.pop()
            elif op == '-':
                neg = True
            else:
                num = int(op)
                q.append(num if not neg else -num)
                neg = False
        return sum(q)
