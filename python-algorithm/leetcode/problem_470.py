"""470. Implement Rand10() Using Rand7()
https://leetcode.com/problems/implement-rand10-using-rand7/
"""
import random


class Solution:
    def rand10(self) -> int:
        def rand7() -> int:
            return random.randrange(1, 8)

        while True:
            row = rand7()
            col = rand7()
            pos = (row - 1) * 7 + col
            if pos <= 40:
                return (pos - 1) % 10 + 1
