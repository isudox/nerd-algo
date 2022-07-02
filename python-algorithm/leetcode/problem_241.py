"""241. Different Ways to Add Parentheses
https://leetcode.com/problems/different-ways-to-add-parentheses/
"""
from typing import List


class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        def split(start: int, end: int) -> List[int]:
            ret = []
            has_ops = False
            for i in range(start, end):
                if expression[i] in ('+', '-', '*'):
                    has_ops = True
                    left = split(start, i)
                    right = split(i + 1, end)
                    for x in left:
                        for y in right:
                            if expression[i] == '+':
                                ret.append(x + y)
                            elif expression[i] == '-':
                                ret.append(x - y)
                            else:
                                ret.append(x * y)
            if not has_ops:
                ret.append(int(expression[start:end]))
            return ret

        return split(0, len(expression))
