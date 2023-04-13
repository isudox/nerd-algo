"""1725. Number Of Rectangles That Can Form The Largest Square
https://leetcode.com/problems/number-of-rectangles-that-can-form-the-largest-square/
"""
from typing import List


def count_good_rectangles(rectangles: List[List[int]]) -> int:
    k = min(rectangles[0])
    for l, w in rectangles:
        k = max(k, min(l, w))
    ans = 0
    for l, w in rectangles:
        if l >= k and w >= k:
            ans += 1
    return ans
