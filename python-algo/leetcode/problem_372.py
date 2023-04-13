"""372. Super Pow
https://leetcode.com/problems/super-pow/
"""
from typing import List


def super_pow(a: int, b: List[int]) -> int:
    ans = 1
    base = a % 1337
    for i in range(len(b) - 1, -1, -1):
        num = b[i]
        for j in range(num):
            ans = (ans * base) % 1337
        next_base = 1
        for k in range(10):
            next_base = (next_base * base) % 1337
        base = next_base
    return ans


if __name__ == '__main__':
    print(super_pow(2, [1, 0]))
