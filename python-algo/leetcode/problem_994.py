"""994. Rotting Oranges
https://leetcode.com/problems/rotting-oranges/
"""
from typing import List


class Solution:
    def oranges_rotting(self, grid: List[List[int]]) -> int:
        ans = 0
        queue = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append([i, j])
        while queue:
            n = len(queue)
            is_end = True
            for _ in range(n):
                x, y = queue.pop(0)
                for d in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                    nx, ny = x + d[0], y + d[1],
                    if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        queue.append([nx, ny])
                        is_end = False
            if not is_end:
                ans += 1
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1
        return ans


if __name__ == '__main__':
    sol = Solution()
    print(sol.oranges_rotting([[2,1,1],
                               [1,1,0],
                               [0,1,1]]))
