package com.leetcode;

import java.util.Stack;

/**
 * 85. Maximal Rectangle
 * https://leetcode.com/problems/maximal-rectangle/
 */
public class Problem85 {

    private int ans;
    private char[][] matrix;

    public int maximalRectangle(char[][] matrix) {
        if (matrix == null || matrix[0] == null) {
            return 0;
        }
        int rows = matrix.length, cols = matrix[0].length;
        int[] heights = new int[cols];
        int ans = 0;
        for (int row = 0; row < rows; row++) {
            for (int col = 0; col < cols; col++) {
                if (matrix[row][col] == 0) {
                    heights[col] = 0;
                } else {
                    heights[col]++;
                }
            }
            ans = Math.max(ans, helper(heights));
        }
        return ans;
    }

    private int helper(int[] heights) {
        int ret = 0;
        Stack<Integer> stack = new Stack<>();
        int p = 0;
        while (p < heights.length) {
            if (stack.isEmpty()) {
                stack.push(p);
                p++;
            } else {
                int peek = stack.peek();
                if (heights[p] >= heights[peek]) {
                    stack.push(p);
                    p++;
                } else {
                    int h = heights[stack.pop()];

                }
            }
        }
        return ret;
    }
}
