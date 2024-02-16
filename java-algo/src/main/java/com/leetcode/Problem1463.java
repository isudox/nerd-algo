package com.leetcode;

import java.util.Arrays;

/**
 * 1463. Cherry Pickup II
 * https://leetcode.com/problems/cherry-pickup-ii/
 */
public class Problem1463 {
    public int cherryPickup(int[][] grid) {
        int m = grid.length, n = grid[0].length;
        int[][][] dp = new int[m][n][n];
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                Arrays.fill(dp[i][j], -1);
            }
        }
        return dfs(grid, dp, 0, 0, n - 1);
    }

    private int dfs(int[][] grid, int[][][] dp, int i, int j, int k) {
        if (dp[i][j][k] >= 0) {
            return dp[i][j][k];
        }
        int cur = j == k ? grid[i][j] : grid[i][j] + grid[i][k];
        if (i == grid.length - 1) {
            return cur;
        }
        int ret = 0;
        int[] dirs = {-1, 1, 0};
        for (int dj : dirs) {
            int nj = j + dj;
            if (nj < 0 || nj >= grid[0].length) {
                continue;
            }
            for (int dk : dirs) {
                int nk = k + dk;
                if (nk >= 0 && nk < grid[1].length) {
                    ret = Math.max(ret, dfs(grid, dp, i + 1, nj, nk));
                }
            }
        }
        return dp[i][j][k] = ret + cur;
    }
}
