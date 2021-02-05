"""803. Bricks Falling When Hit
https://leetcode.com/problems/bricks-falling-when-hit/

Example 1:

Input: grid = [[1,0,0,0],[1,1,1,0]], hits = [[1,0]]
Output: [2]
Explanation: Starting with the grid:
[[1,0,0,0],
 [1,1,1,0]]
We erase the underlined brick at (1,0), resulting in the grid:
[[1,0,0,0],
 [0,1,1,0]]
The two underlined bricks are no longer stable as they are no longer
connected to the top nor adjacent to another stable brick, so they will fall.
The resulting grid is:
[[1,0,0,0],
 [0,0,0,0]]
Hence the result is [2].

Constraints:

    m == grid.length
    n == grid[i].length
    1 <= m, n <= 200
    grid[i][j] is 0 or 1.
    1 <= hits.length <= 4 * 10^4
    hits[i].length == 2
    0 <= xi <= m - 1
    0 <= yi <= n - 1
    All (xi, yi) are unique
"""
from typing import List


class Solution:
    def hit_bricks(self, grid: List[List[int]], hits: List[List[int]]) -> List[int]:
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
            return x * cols + y

        def get_top():
            pass

        rows, cols = len(grid), len(grid[0])
        size = rows * cols
        uf, rank = list(range(size + 1)), [1] * (size + 1)
        new_grid = [row[:] for row in grid]
        for i, j in hits:
            new_grid[i][j] = 0
        for i, row in enumerate(new_grid):
            for j, val in enumerate(row):
                if val > 0:
                    if i == 0:
                        union(get_pos(i, j), size)
                    elif new_grid[i - 1][j] == 1:
                        union(get_pos(i, j), get_pos(i - 1, j))
                    if j > 0 and new_grid[i][j - 1] == 1:
                        union(get_pos(i, j), get_pos(i, j - 1))
        ans = []
        dirs = [[0,1],[0, -1], [1,0],[-1,0]]
        for i, j in reversed(hits):
            if grid[i][j] > 0:
                for ni, nj in dirs:
                    next_i, next_j = i + ni, j + nj
                    if 0 <= next_i < rows and 0 <= next_j < cols and new_grid[next_i][next_j]:
                        union(get_pos(i, j), get_pos(next_i, next_j))
                if i == 0:
                    union(get_pos(i, j), size)
                new_grid[i][j] = 1
                ans.append()
            else:
                ans.append(0)
        return ans[::-1]
                        


if __name__ == "__main__":
    sol = Solution()
    print(sol.hit_bricks([[1, 0, 0, 0], [1, 1, 1, 0]], [[1, 0]]))  # [2]
    print(sol.hit_bricks([[1, 0, 0, 0], [1, 1, 0, 0]], [[1, 1], [1, 0]]))  # [0,0]
