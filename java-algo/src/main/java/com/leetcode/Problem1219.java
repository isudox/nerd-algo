package com.leetcode;

/**
 * 1219. Path with Maximum Gold
 * https://leetcode.com/problems/path-with-maximum-gold/
 */
public class Problem1219 {
    int[][] dirs = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};

    public int getMaximumGold(int[][] grid) {
        int m = grid.length, n = grid[0].length;
        boolean[][] visited = new boolean[m][n];
        int ans = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] > 0) {
                    ans = Math.max(ans, backtrack(grid, visited, i, j));
                }
            }
        }
        return ans;
    }

    private int backtrack(int[][] grid, boolean[][] visited, int x, int y) {
        int ret = 0;
        visited[x][y] = true;
        for (int[] d : dirs) {
            int nx = x + d[0], ny = y + d[1];
            if (0 <= nx && nx < grid.length && 0 <= ny && ny < grid[0].length && !visited[nx][ny] && grid[nx][ny] > 0) {
                ret = Math.max(ret, backtrack(grid, visited, nx, ny));
            }
        }
        visited[x][y] = false;
        return ret + grid[x][y];
    }
}
