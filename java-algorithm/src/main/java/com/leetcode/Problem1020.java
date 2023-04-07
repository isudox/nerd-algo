package com.leetcode;

/**
 * 1020. Number of Enclaves
 * https://leetcode.com/problems/number-of-enclaves/
 */
public class Problem1020 {
    private int[][] dirs = new int[][]{{0, 1}, {0, -1}, {1, 0}, {-1, 0}};

    public int numEnclaves(int[][] grid) {
        int ans = 0, m = grid.length, n = grid[0].length;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 1 && (i == 0 || i == m - 1 || j == 0 || j == n - 1)) {
                    dfs(grid, i, j);
                }
            }
        }
        for (int[] row : grid) {
            for (int e : row) {
                if (e == 1) {
                    ans++;
                }
            }
        }
        return ans;
    }

    private void dfs(int[][] grid, int i, int j) {
        grid[i][j] = 0;
        for (int[] d : dirs) {
            int di = i + d[0], dj = j + d[1];
            if (0 <= di && di < grid.length && 0 <= dj && dj < grid[0].length && grid[di][dj] == 1) {
                dfs(grid, di, dj);
            }
        }
    }
}
