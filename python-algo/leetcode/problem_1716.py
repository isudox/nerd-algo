"""1716. Calculate Money in Leetcode Bank
https://leetcode.com/problems/calculate-money-in-leetcode-bank/
"""


def total_money(n: int) -> int:
    a, b = divmod(n, 7)
    start, end = 28, 28 + (a - 1) * 7
    ans = (start + end) * a // 2
    c = a + 1
    d = a + b
    return ans + (c + d) * b // 2
