"""84. Largest Rectangle in Histogram
https://leetcode.com/problems/largest-rectangle-in-histogram/

Given n non-negative integers representing the histogram's bar height where
the width of each bar is 1, find the area of largest rectangle in the
histogram.




Above is a histogram where width of each bar is 1, given height =
[2,1,5,6,2,3].




The largest rectangle is shown in the shaded area, which has area = 10
unit.



Example:


Input: [2,1,5,6,2,3]
Output: 10
"""
from typing import List


class Solution:
    def largest_rectangle_area(self, heights: List[int]) -> int:
        if not heights:
            return 0
        length = len(heights)
        left_idx = [0] * length
        right_idx = [0] * length
        for i in range(length):
            p = i - 1
            while p >= 0 and heights[p] >= heights[i]:
                p = left_idx[p]
            left_idx[i] = p
        for i in range(length - 1, -1, -1):
            p = i + 1
            while p < length and heights[p] >= heights[i]:
                p = right_idx[p]
            right_idx[i] = p
        max_area = 0
        for i in range(length):
            max_area = max(max_area,
                           heights[i] * (right_idx[i] - left_idx[i] - 1))
        return max_area

    def brute_force(self, heights: List[int]) -> int:
        i = length = len(heights)
        if i == 0:
            return 0
        max_area = 0
        while i > 0:
            for start in range(0, length - i + 1):
                cur_area = min(heights[start: start + i]) * i
                max_area = max(max_area, cur_area)
            i -= 1

        return max_area
