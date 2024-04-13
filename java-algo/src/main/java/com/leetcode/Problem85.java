package com.leetcode;

/**
 * 85. Maximal Rectangle
 * https://leetcode.com/problems/maximal-rectangle/
 */
public class Problem85 {
    public int maximalRectangle(char[][] matrix) {
        if (matrix == null || matrix.length == 0 || matrix[0].length == 0) {
            return 0;
        }
        int rows = matrix.length, cols = matrix[0].length;
        int[] heights = new int[cols];
        int ans = 0;
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (matrix[i][j] == '1') {
                    heights[j]++;
                } else {
                    heights[j] = 0;
                }
            }
            for (int x = 0; x < heights.length; x++) {
                for (int y = x, minHeight = Integer.MAX_VALUE; y < heights.length; y++) {
                    minHeight = Math.min(minHeight, heights[y]);
                    ans = Math.max(ans, minHeight * (y - x + 1));
                }
            }
        }
        return ans;
    }
}
