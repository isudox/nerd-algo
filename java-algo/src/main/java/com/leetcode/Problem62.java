package com.leetcode;

/**
 * 62. Unique Paths
 * https://leetcode.com/problems/unique-paths/
 *
 * A robot is located at the top-left corner of a m * n grid
 * (marked 'Start' in the diagram below).
 *
 * The robot can only move either down or right at any point in time.
 * The robot is trying to reach the bottom-right corner of the grid
 *  (marked 'Finish' in the diagram below).
 *
 * How many possible unique paths are there?
 *
 * Above is a 7 x 3 grid. How many possible unique paths are there?
 *
 * Note: m and n will be at most 100.
 *
 * Example 1:
 *
 * Input: m = 2, n = 3
 * Output: 3
 * Explanation:
 * From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
 * 1. Right -> Right -> Down
 * 2. Right -> Down -> Right
 * 3. Down -> Right -> Right
 *
 * Example 2:
 *
 * Input: m = 7, n = 3
 * Output: 28
 */
public class Problem62 {
    public int uniquePaths(int m, int n) {
        // dp[i][j] = the ways from grid[0][0] to grid[i][j]
        int[][] dp = new int[m][n];
        for (int i = 0; i < n; i++)
            dp[0][i] = 1;
        for (int i = 0; i < m; i++)
            dp[i][0] = 1;
        for (int row = 1; row < m; row++)
            for (int col = 1; col < n; col++)
                dp[row][col] = dp[row - 1][col] + dp[row][col - 1];
        return dp[m - 1][n - 1];
    }
}
