package com.leetcode;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**
 * 417. Pacific Atlantic Water Flow
 * https://leetcode.com/problems/pacific-atlantic-water-flow/
 */
public class Problem417 {
    private final int[][] DIRS = new int[][]{{0, 1}, {0, -1}, {1, 0}, {-1, 0}};

    public List<List<Integer>> pacificAtlantic(int[][] heights) {
        int m = heights.length, n = heights[0].length;
        boolean[][] pacific = new boolean[m][n];
        boolean[][] atlantic = new boolean[m][n];
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (i == 0 || j == 0) {  // pacific shore -> atlantic shore
                    dfs(heights, atlantic, i, j, 0);
                }
                if (i == m - 1 || j == n - 1) { // atlantic shore -> pacific shore
                    dfs(heights, pacific, i, j, 0);
                }
            }
        }
        List<List<Integer>> ans = new ArrayList<>();
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (pacific[i][j] && atlantic[i][j]) {
                    ans.add(Arrays.asList(i, j));
                }
            }
        }
        return ans;
    }

    private void dfs(int[][] grid, boolean[][] visited, int x, int y, int least) {
        int m = grid.length, n = grid[0].length;
        if (x < 0 || x >= m || y < 0 || y >= n || visited[x][y] || grid[x][y] < least) {
            return;
        }
        visited[x][y] = true;
        for (int[] dir : DIRS) {
            dfs(grid, visited, x + dir[0], y + dir[1], grid[x][y]);
        }
    }
}
