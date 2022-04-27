package com.leetcode;

/**
 * 883. Projection Area of 3D Shapes
 */
public class Problem883 {
    public int projectionArea(int[][] grid) {
        int top = 0, front = 0, side = 0;
        int m = grid.length, n = grid[0].length;
        for (int[] row : grid) {
            int tmp = 0;
            for (int i = 0; i < n; i++) {
                if (row[i] > 0) {
                    top++;
                    tmp = Math.max(tmp, row[i]);
                }
            }
            front += tmp;
        }
        for (int i = 0; i < n; i++) {
            int tmp = 0;
            for (int j = 0; j < m; j++) {
                tmp = Math.max(tmp, grid[j][i]);
            }
            side += tmp;
        }
        return top + front + side;
    }
}
