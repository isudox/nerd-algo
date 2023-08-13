"""63. Unique Paths II
https://leetcode.com/problems/unique-paths-ii/
"""
from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                    continue
                dp[i][j] += dp[i - 1][j] if i >= 1 else 0
                dp[i][j] += dp[i][j - 1] if j >= 1 else 0
        return dp[-1][-1]

    def unique_paths_with_obstacles(self, obstacle_grid: List[List[int]]):
        rows, cols = len(obstacle_grid), len(obstacle_grid[0])
        dp = [[1] * cols for _ in range(rows)]
        for _ in range(cols):
            if obstacle_grid[0][_] == 1:
                dp[0][_] = 0
            else:
                dp[0][_] = dp[0][_ - 1]
        for _ in range(rows):
            if obstacle_grid[_][0] == 1:
                dp[_][0] = 0
            else:
                dp[_][0] = dp[_ - 1][0]
        for i in range(1, rows):
            for j in range(1, cols):
                if obstacle_grid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i][j - 1] + dp[i - 1][j]
        return dp[rows - 1][cols - 1]

    def uniquePathsWithObstacles2(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid or not obstacleGrid[0]:
            return 0
        dp = [1] + [0] * (len(obstacleGrid[0]) - 1)
        for row in obstacleGrid:
            dp[0] = 0 if row[0] == 1 else dp[0]
            for i in range(1, len(obstacleGrid[0])):
                dp[i] = 0 if row[i] == 1 else dp[i] + dp[i - 1]
        return dp[-1]


if __name__ == '__main__':
    sol = Solution()
    print(sol.uniquePathsWithObstacles2([[0, 0, 0], [0, 1, 0], [0, 0, 0]]))
