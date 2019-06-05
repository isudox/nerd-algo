"""84. Largest Rectangle in Histogram
https://leetcode.com/problems/largest-rectangle-in-histogram/


Given n non-negative integers representing the histogram's bar height where
the width of each bar is 1, find the area of largest rectangle in the
histogram.

           _
|^       _| |
|       | | |
|       | | |  _
|    _  | | |_| |
|   | |_| | | | |
|___|_|_|_|_|_|_|____>

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
    def largest_rectangle_area_1(self, heights: List[int]) -> int:
        # time complexity: O(N)
        max_area = 0
        stack = []
        i, length = 0, len(heights)
        while i < length:
            if not stack or (heights[stack[-1]] <= heights[i]):
                stack.append(i)
                i += 1
            else:
                top = stack.pop()
                cur_area = heights[top] * (i - stack[-1] - 1 if stack else i)
                max_area = max(max_area, cur_area)
        while stack:
            top = stack.pop()
            cur_area = heights[top] * (i - stack[-1] - 1 if stack else i)
            max_area = max(max_area, cur_area)

        return max_area

    def largest_rectangle_area_2(self, heights: List[int]) -> int:
        if not heights:
            return 0
        length = len(heights)
        left_border_idx = [0] * length
        right_border_idx = [0] * length
        for i in range(length):
            p = i - 1
            while p >= 0 and heights[p] >= heights[i]:
                p = left_border_idx[p]
            left_border_idx[i] = p
        for i in range(length - 1, -1, -1):
            p = i + 1
            while p < length and heights[p] >= heights[i]:
                p = right_border_idx[p]
            right_border_idx[i] = p
        max_area = 0
        for i in range(length):
            max_area = max(max_area,
                           heights[i] * (right_border_idx[i] -
                                         left_border_idx[i] - 1))
        return max_area

    def brute_force(self, heights: List[int]) -> int:
        # time complexity: O(N^2)
        length = len(heights)
        max_area = 0
        for i in range(length):
            left = right = i
            while left - 1 >= 0 and heights[left - 1] >= heights[i]:
                left -= 1
            while right + 1 < length and heights[right + 1] >= heights[i]:
                right += 1
            max_area = max(max_area, (right - left + 1) * heights[i])
        return max_area

