package com.leetcode;

/**
 * 200. Number of Islands
 * https://leetcode.com/problems/number-of-islands/
 */
class Problem200 {
    private static final int[][] DIRS = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
    public int numIslands(char[][] grid) {
        int ans = 0;
        int m = grid.length, n = grid[0].length;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (dfs(grid, i, j)) ans++;
            }
        }
        return ans;
    }

    private boolean dfs(char[][] grid, int x, int y) {
        if (grid[x][y] == '0') return false;
        grid[x][y] = '0';
        for (int[] dir : DIRS) {
            int nx = x + dir[0], ny = y + dir[1];
            if (0 <= nx && nx < grid.length && 0 <= ny && ny < grid[0].length && grid[nx][ny] == '1') {
                dfs(grid, nx, ny);
            }
        }
        return true;
    }
}
