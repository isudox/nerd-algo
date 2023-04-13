"""391. Perfect Rectangle
https://leetcode.com/problems/perfect-rectangle/
"""
from typing import List


class Solution:
    def is_rectangle_cover(self, rectangles: List[List[int]]) -> bool:
        def cal(rec: List[int]) -> int:
            x, y, a, b = rec
            return abs(x - a) * abs(y - b)
        sum_area = 0
        lo_x, lo_y, hi_a, hi_b = float('inf'), float('inf'), float('-inf'), float('-inf')
        for rectangle in rectangles:
            sum_area += cal(rectangle)

        return True
