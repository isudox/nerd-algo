package com.leetcode;

/**
 * 1254. Number of Closed Islands
 * https://leetcode.com/problems/number-of-closed-islands/
 */
public class Problem1254 {
    public int closedIsland(int[][] grid) {
        int ans = 0;
        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[0].length; j++) {
                if (grid[i][j] == 0) {
                    ans += dfs(grid, i, j) ? 1 : 0;
                }
            }
        }
        return ans;
    }

    private boolean dfs(int[][] grid, int i, int j) {
        if (i < 0 || i >= grid.length || j < 0 || j >= grid[0].length) {
            return false;
        }
        if (grid[i][j] == 0) {
            grid[i][j] = 1;
            boolean u = dfs(grid, i - 1, j);
            boolean d = dfs(grid, i + 1, j);
            boolean l = dfs(grid, i, j - 1);
            boolean r = dfs(grid, i, j + 1);
            return u && d && l && r;
        }
        return true;
    }
}
