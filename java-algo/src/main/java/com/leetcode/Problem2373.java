package com.leetcode;

/**
 * 2373. Largest Local Values in a Matrix
 * https://leetcode.com/problems/largest-local-values-in-a-matrix
 */
public class Problem2373 {
    public int[][] largestLocal(int[][] grid) {
        int n = grid.length;
        int[][] ans = new int[n - 2][n - 2];
        for (int i = 0; i < n - 2; i++) {
            for (int j = 0; j < n - 2; j++) {
                ans[i][j] = helper(grid, i + 1, j + 1);
            }
        }
        return ans;
    }

    private int helper(int[][] grid, int x, int y) {
        int ret = grid[x][y];
        for (int i = x - 1; i <= x + 1; i++) {
            for (int j = y - 1; j <= y + 1; j++) {
                if (grid[i][j] > ret) {
                    ret = grid[i][j];
                }
            }
        }
        return ret;
    }
}
