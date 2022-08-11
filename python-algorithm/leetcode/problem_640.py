"""640. Solve the Equation
https://leetcode.com/problems/solve-the-equation/
The equation contains only '+', '-', the variable 'x' and its coefficient
Input: equation = "x+5-3+x=6+x-2"
Output: "x=2"
"""
from typing import List


class Solution:
    def solveEquation(self, equation: str) -> str:
        def parse(expr: str) -> List[int]:
            ret = [0, 0]
            pos = 0
            flag = 1
            for i, ch in enumerate(expr):
                if ch == 'x':
                    num = expr[pos:i]
                    ret[0] += flag * (1 if num == '' else int(num))
                    pos = i + 1
                if ch == '+' or ch == '-':
                    num = expr[pos:i]
                    if num != '':
                        ret[1] += int(num) * flag
                    flag = 1 if ch == '+' else -1
                    pos = i + 1
            return ret

        left, right = equation.split('=')
        left_x, left_num = parse(left + '+0')
        right_x, right_num = parse(right + '+0')
        diff_x = left_x - right_x
        diff_num = right_num - left_num
        if diff_x == 0:
            return 'Infinite solutions' if diff_num == 0 else 'No solution'
        return str.format('x={}', diff_num // diff_x)
