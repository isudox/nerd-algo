package com.leetcode;

/**
 * 63. Unique Paths II
 * https://leetcode.com/problems/unique-paths-ii/
 *
 *
 * A robot is located at the top-left corner of a m x n grid
 * (marked 'Start' in the diagram below).
 *
 * The robot can only move either down or right at any point in time.
 * The robot is trying to reach the bottom-right corner of the grid
 * (marked 'Finish' in the diagram below).
 *
 * Now consider if some obstacles are added to the grids.
 * How many unique paths would there be?
 *
 *
 *
 * An obstacle and empty space is marked as 1 and 0 respectively in the grid.
 *
 * Note: m and n will be at most 100.
 *
 * Example 1:
 *
 * Input:
 * [
 *   [0,0,0],
 *   [0,1,0],
 *   [0,0,0]
 * ]
 * Output: 2
 * Explanation:
 * There is one obstacle in the middle of the 3x3 grid above.
 * There are two ways to reach the bottom-right corner:
 * 1. Right -> Right -> Down -> Down
 * 2. Down -> Down -> Right -> Right
 */
public class Problem63 {
    public int uniquePathsWithObstacles(int[][] obstacleGrid) {
        int rows = obstacleGrid.length, cols = obstacleGrid[0].length;
        // dp[i][j] means how many roads from start to grid[i][j]
        int[][] dp = new int[rows][cols];
        dp[0][0] = obstacleGrid[0][0] == 0 ? 1 : 0;
        for (int i = 1; i < cols; i++) {
            if (obstacleGrid[0][i] == 0 )
                dp[0][i] = dp[0][i - 1];
        }
        for (int i = 1; i < rows; i++) {
            if (obstacleGrid[i][0] == 0)
                dp[i][0] = dp[i - 1][0];
        }
        for (int i = 1; i < rows; i++) {
            for (int j = 1; j < cols; j++) {
                if (obstacleGrid[i][j] == 0)
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1];
            }
        }
        return dp[rows - 1][cols - 1];
    }

    private static final int[][] DIRS = new int[][]{{0, 1}, {1, 0}};
    private static int[][] memo;

    public int uniquePathsWithObstacles2(int[][] grid) {
        int m = grid.length, n = grid[0].length;
        if (grid[0][0] != 0 || grid[m - 1][n - 1] != 0) {
            return 0;
        }
        memo = new int[m][n];
        return dfs(grid, 0, 0);
    }

    private int dfs(int[][] grid, int x, int y) {
        if (memo[x][y] > 0) {
            return memo[x][y];
        }
        if (x == grid.length - 1 && y == grid[0].length - 1) {
            return 1;
        }
        int cnt = 0;
        for (int[] d : DIRS) {
            int nx = x + d[0], ny = y + d[1];
            if (0 <= nx && nx < grid.length && 0 <= ny && ny < grid[0].length && grid[nx][ny] == 0) {
                cnt += dfs(grid, nx, ny);
            }
        }
        return memo[x][y] = cnt;
    }
}
