"""1009. Complement of Base 10 Integer
https://leetcode.com/problems/complement-of-base-10-integer/
"""


def bitwise_complement(n: int) -> int:
    if n == 0:
        return 1
    ans = 0
    pos = 0
    while n:
        bit = n & 0b1
        if bit == 0:
            ans += (1 << pos)
        pos += 1
        n >>= 1
    return ans
