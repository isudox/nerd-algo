# -*- coding: utf-8 -*-
"""959. Regions Cut By Slashes
https://leetcode.com/problems/regions-cut-by-slashes/

In a N x N grid composed of 1 x 1 squares, each 1 x 1 square consists of a /, \,
or blank space.  These characters divide the square into contiguous regions.

(Note that backslash characters are escaped, so a \ is represented as "\\".)

Return the number of regions.



Example 1:
  Input:
  [
    " /",
    "/ "
  ]
  Output: 2
  Explanation: The 2x2 grid is as follows:

Example 2:

  Input:
  [
    " /",
    "  "
  ]
  Output: 1
  Explanation: The 2x2 grid is as follows:

Example 3:

  Input:
  [
    "\\/",
    "/\\"
  ]
  Output: 4
  Explanation: (Recall that because \ characters are escaped,
  "\\/" refers to \/, and "/\\" refers to /\.)
  The 2x2 grid is as follows:

Example 4:

  Input:
  [
    "/\\",
    "\\/"
  ]
  Output: 5
  Explanation: (Recall that because \ characters are escaped,
  "/\\" refers to /\, and "\\/" refers to \/.)
  The 2x2 grid is as follows:

Example 5:

  Input:
  [
    "//",
    "/ "
  ]
  Output: 3
  Explanation: The 2x2 grid is as follows:


Note:

  1 <= grid.length == grid[0].length <= 30
  grid[i][j] is either '/', '\', or ' '.
"""
from typing import List


class Solution:
    def regions_by_slashes(self, grid: List[str]) -> int:
        def union(x: int, y: int):
            fx, fy = find(x), find(y)
            if rank[fx] < rank[fy]:
                fx, fy = fy, fx
            uf[fy] = fx
            rank[fx] += rank[fy]

        def find(x: int) -> int:
            if uf[x] != x:
                uf[x] = find(uf[x])
            return uf[x]

        rows, cols = len(grid), len(grid[0])
        n = (rows + 1) ** 2
        uf, rank = list(range(n)), [1] * n
        ans = 0
        for i in range(n):
            union(0, i)
        for i in range(rows):
            j = 0
            while j < cols:
                cur = grid[i][j]
                if cur == '/':
                    j += 1
                    union((rows + 1) * i + j + 1, (rows + 1) * (i + 1) + j)
                elif cur == ' ':
                    j += 1
                elif cur == '\\':
                    j += 2
                    union((rows + 1) * i + j, (rows + 1) * (i + 1) + j + 1)

        return ans
