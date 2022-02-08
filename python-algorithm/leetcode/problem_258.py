"""258. Add Digits
https://leetcode.com/problems/add-digits/
"""


def add_digits(num: int) -> int:
    while num > 9:
        cur = 0
        while num > 0:
            num, a = divmod(num, 10)
            cur += a
        num = cur
    return num
