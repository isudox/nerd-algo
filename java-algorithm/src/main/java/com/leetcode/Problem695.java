package com.leetcode;

/**
 * 695. Max Area of Island
 * https://leetcode.com/problems/max-area-of-island/
 */
public class Problem695 {
    public int maxAreaOfIsland(int[][] grid) {
        int ans = 0;
        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[0].length; j++) {
                if (grid[i][j] == 1) {
                    int area = dfs(grid, i, j);
                    if (area > ans) ans = area;
                }
            }
        }
        return ans;
    }

    private int dfs(int[][] grid, int x, int y) {
        int area = 1;
        grid[x][y] = 0;
        int[][] dirs = new int[][]{{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
        for (int[] d : dirs) {
            int nx = x + d[0], ny = y + d[1];
            if (0 <= nx && nx < grid.length && 0 <= ny && ny < grid[0].length && grid[nx][ny] == 1) {
                area += dfs(grid, nx, ny);
            }
        }
        return area;
    }
}
