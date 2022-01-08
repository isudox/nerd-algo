"""89. Gray Code
https://leetcode.com/problems/gray-code/
"""
from typing import List


def gray_code(n: int) -> List[int]:
    ans = []
    size = 1 << n
    for i in range(size):
        ans.append(i ^ (i >> 1))
    return ans
