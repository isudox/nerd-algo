"""400. Nth Digit
https://leetcode.com/problems/nth-digit/
"""


class Solution:
    def findNthDigit(self, n: int) -> int:
        x = 1
        cnt = 9
        while n > x * cnt:
            n -= x * cnt
            x += 1
            cnt *= 10
        start = 10 ** (x - 1)
        pos = n - 1
        num = start + pos // x
        need = pos % x
        return num // 10 ** (x - need - 1) % 10
