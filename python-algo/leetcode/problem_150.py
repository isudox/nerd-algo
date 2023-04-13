"""150. Evaluate Reverse Polish Notation
https://leetcode.com/problems/evaluate-reverse-polish-notation/
"""
from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = ('+', '-', '*', '/')
        for t in tokens:
            if t in ops:
                a = stack.pop()
                b = stack.pop()
                if t == '+':
                    c = a + b
                elif t == '-':
                    c = b - a
                elif t == '*':
                    c = b * a
                else:
                    c = int(b / a)
                stack.append(c)
            else:
                stack.append(int(t))
        return stack[0]
