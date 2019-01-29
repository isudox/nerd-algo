# -*- coding: utf-8 -*-


class Solution:
    def unique_paths_iii(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        lines = len(grid)
        columns = len(grid[0])
        zero_count = 0
        start_i = start_j = 0
        i = 0
        while i < lines:
            j = 0
            while j < columns:
                if grid[i][j] == 0:
                    zero_count += 1
                elif grid[i][j] == 1:
                    start_i, start_j = i, j
                j += 1
            i += 1
        visited = [[False for _ in range(columns)] for _ in range(lines)]
        visited[start_i][start_j] = True

        def backtrack(visited, i, j, zero):
            d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for x, y in d:
                x += i
                y +=j
