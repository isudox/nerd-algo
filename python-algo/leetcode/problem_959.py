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

        def get_pos(x: int, y: int) -> int:
            return (rows + 1) * x + y

        rows = cols = len(grid)
        n = (rows + 1) ** 2
        uf, rank = list(range(n)), [1] * n
        first_pos, last_pos = get_pos(0, 0), get_pos(rows, rows)
        for i in range(rows + 1):
            union(get_pos(0, i), first_pos)
            union(get_pos(i, 0), first_pos)
            union(get_pos(rows, i), last_pos)
            union(get_pos(i, rows), last_pos)
        ans = 1
        for i in range(rows):
            for j in range(cols):
                char = grid[i][j]
                if char != ' ':
                    if char == '/':
                        upper_point = get_pos(i, j + 1)
                        lower_point = get_pos(i + 1, j)
                    else:
                        upper_point = get_pos(i, j)
                        lower_point = get_pos(i + 1, j + 1)
                    if find(upper_point) == find(lower_point):
                        ans += 1
                    else:
                        union(upper_point, lower_point)
        return ans
