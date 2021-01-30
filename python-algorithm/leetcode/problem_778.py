"""778. Swim in Rising Water
https://leetcode.com/problems/swim-in-rising-water/

On an N x N grid, each square grid[i][j] represents the elevation at that point (i,j).

Now rain starts to fall. At time t, the depth of the water everywhere is t.
You can swim from a square to another 4-directionally adjacent square if and
only if the elevation of both squares individually are at most t.
You can swim infinite distance in zero time. Of course, you must stay
within the boundaries of the grid during your swim.

You start at the top left square (0, 0). What is the least time until you
can reach the bottom right square (N-1, N-1)?

Example 1:

Input: [[0,2],[1,3]]
Output: 3
Explanation:
At time 0, you are in grid location (0, 0).
You cannot go anywhere else because 4-directionally adjacent neighbors have
a higher elevation than t = 0.

You cannot reach point (1, 1) until time 3.
When the depth of water is 3, we can swim anywhere inside the grid.

Example 2:

Input: [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]
Output: 16
Explanation:
 0  1  2  3  4
24 23 22 21  5
12 13 14 15 16
11 17 18 19 20
10  9  8  7  6

The final route is marked in bold.
We need to wait until time 16 so that (0, 0) and (4, 4) are connected.
Note:

2 <= N <= 50.
grid[i][j] is a permutation of [0, ..., N*N - 1].
"""
from typing import List


class Solution:
    def swim_in_water(self, grid: List[List[int]]) -> int:
        def dfs(x: int, y: int, cur_t: int, limit_t: int):
            visited[x][y] = True
            for nx, ny in dirs:
                next_x, next_y = x + nx, y + ny
                if 0 <= next_x < rows and 0 <= next_y < cols and not visited[next_x][next_y] and grid[next_x][next_y] <= limit_t:
                    if grid[next_x][next_y] > cur_t:
                        dfs(next_x, next_y, grid[next_x][next_y], limit_t)
                    else:
                        dfs(next_x, next_y, cur_t, limit_t)

        max_t, min_t = 0, grid[0][0]
        rows, cols = len(grid), len(grid[0]),
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] > max_t:
                    max_t = grid[i][j]
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        visited = list()
        while min_t < max_t:
            mid_t = (max_t + min_t) // 2
            visited = [[False] * cols for _ in range(rows)]
            dfs(0, 0, grid[0][0], mid_t)
            if visited[-1][-1]:
                max_t = mid_t
            else:
                min_t = mid_t + 1
        return min_t
