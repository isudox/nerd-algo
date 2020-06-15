"""221. Maximal Square
https://leetcode.com/problems/maximal-square/

Given a 2D binary matrix filled with 0's and 1's,
find the largest square containing only 1's and return its area.

Example:

Input:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

Output: 4
"""
from typing import List


class Solution:
    def maximal_square(self, matrix: List[List[str]]) -> int:
        def find_square(x: int, y: int) -> int:
            z = 0
            while x + z < rows and y + z < cols:
                for m in range(x, x + z + 1):
                    if matrix[m][y + z] != '1':
                        return z * z
                for n in range(y, y + z + 1):
                    if matrix[x + z][n] != '1':
                        return z * z
                z += 1
            return z * z

        """
        brute force.
        :param matrix:
        :return:
        """
        if not matrix or not matrix[0]:
            return 0
        max_area = 0
        rows, cols = len(matrix), len(matrix[0])
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == '1':
                    max_area = max(max_area, find_square(i, j))
        return max_area

    def maximal_square1(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        rows, cols = len(matrix), len(matrix[0])
        heights = [0] * (cols + 1)
        max_area = 0
        for row in range(rows):
            stack = []
            for col in range(cols + 1):
                if col < cols and matrix[row][col] == "1":
                    heights[col] += 1
                else:
                    heights[col] = 0
                while stack and heights[stack[-1]] >= heights[col]:
                    height = heights[stack.pop()]
                    width = col - stack[-1] - 1 if stack else col
                    cur_area = min(height, width) ** 2
                    max_area = max(max_area, cur_area)
                stack.append(col)
        return max_area
