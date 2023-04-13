"""2022. Convert 1D Array Into 2D Array
https://leetcode.com/problems/convert-1d-array-into-2d-array/
"""
from typing import List


def construct_2d_array(original: List[int], m: int, n: int) -> List[List[int]]:
    size = len(original)
    if m * n != size:
        return []
    ans = [[0] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            k = n * i + j
            ans[i][j] = original[k]
    return ans
