package com.leetcode;

/**
 * 463. Island Perimeter
 * https://leetcode.com/problems/island-perimeter/
 */
public class Problem463 {
    public int islandPerimeter(int[][] grid) {
        int ans = 0;
        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[i].length; j++) {
                if (grid[i][j] == 1) {
                    ans += helper(grid, i, j);
                }
            }
        }
        return ans;
    }

    private int helper(int[][] grid, int x, int y) {
        int count = 0;
        int[][] dirs = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
        for (int[] dir : dirs) {
            int nx = x + dir[0], ny = y + dir[1];
            if (nx < 0 || nx >= grid.length || ny < 0 || ny >= grid[0].length || grid[nx][ny] == 0) {
                count++;
            }
        }
        return count;
    }
}
