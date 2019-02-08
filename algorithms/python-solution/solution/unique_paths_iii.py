# -*- coding: utf-8 -*-
"""980. Unique Paths III
https://leetcode.com/problems/unique-paths-iii/

On a 2-dimensional grid, there are 4 types of squares:

  1 represents the starting square.  There is exactly one starting square.
  2 represents the ending square.  There is exactly one ending square.
  0 represents empty squares we can walk over.
  -1 represents obstacles that we cannot walk over.
  Return the number of 4-directional walks from the starting square to the
  ending square, that walk over every non-obstacle square exactly once.

Example 1:

Input: [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
  Output: 2
  Explanation: We have the following two paths:
  1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2)
  2. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2)

Note:

  1 <= grid.length * grid[0].length <= 20
"""


class Solution:
    def unique_paths_iii(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        lines, columns = len(grid), len(grid[0])
        start_i = start_j = zero_count = ans = 0
        for i in range(lines):
            for j in range(columns):
                if grid[i][j] == 0:
                    zero_count += 1
                elif grid[i][j] == 1:
                    start_i, start_j = i, j
        # visited = [[False] * columns] * lines
        visited = [[False for _ in range(columns)] for _ in range(lines)]
        visited[start_i][start_j] = True

        def backtrack(visited, i, j, zero):
            nonlocal zero_count, ans
            # 4 directions to move
            d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for x, y in d:
                x += i
                y += j
                if 0 <= x < lines and 0 <= y < columns and not visited[x][y] and grid[x][y] != -1:
                    if grid[x][y] == 0:
                        visited[x][y] = True
                        backtrack(visited, x, y, zero + 1)
                        visited[x][y] = False
                    elif zero == zero_count:
                        ans += 1

        backtrack(visited, start_i, start_j, 0)
        return ans


if __name__ == '__main__':
    print(Solution().unique_paths_iii(
        [[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 2, -1]]))
