"""85. Maximal Rectangle
https://leetcode.com/problems/maximal-rectangle/


Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle
containing only 1's and return its area.

Example:


Input:
[
⁠ ["1","0","1","0","0"],
⁠ ["1","0","1","1","1"],
⁠ ["1","1","1","1","1"],
⁠ ["1","0","0","1","0"]
]
Output: 6
"""
from typing import List


class Solution:
    def maximal_rectangle(self, matrix: List[List[str]]) -> int:
        """
        Time complexity O(N^2)
        :param matrix:
        :return:
        """
        if not matrix or not matrix[0]:
            return 0
        rows, cols = len(matrix), len(matrix[0])
        heights = [0] * (cols + 1)
        max_area = 0
        for row in range(rows):
            stack = [-1]
            for col in range(cols + 1):
                if col < cols and matrix[row][col] == "1":
                    heights[col] += 1
                else:
                    heights[col] = 0
                while stack and heights[stack[-1]] >= heights[col]:
                    height = heights[stack.pop()]
                    width = col - stack[-1] - 1 if stack else col
                    cur_area = height * width
                    max_area = max(max_area, cur_area)
                stack.append(col)
        return max_area
