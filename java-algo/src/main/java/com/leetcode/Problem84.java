package com.leetcode;

import java.util.Stack;

/**
 * 84. Largest Rectangle in Histogram
 * https://leetcode.com/problems/largest-rectangle-in-histogram/
 *
 * Given n non-negative integers representing the histogram's bar height where
 * the width of each bar is 1, find the area of largest rectangle in the
 * histogram.
 *
 *            _
 * |^       _| |
 * |       | | |
 * |       | | |  _
 * |    _  | | |_| |
 * |   | |_| | | | |
 * |___|_|_|_|_|_|_|____>
 *
 * Above is a histogram where width of each bar is 1, given height =
 * [2,1,5,6,2,3].
 *
 * The largest rectangle is shown in the shaded area, which has area = 10
 * unit.
 *
 * Example:
 *
 * Input: [2,1,5,6,2,3]
 * Output: 10
 * Constraints:
 *
 * 1 <= heights.length <= 10^5
 * 0 <= heights[i] <= 10^4
 */
public class Problem84 {
    public int largestRectangleArea(int[] heights) {
        Stack<Integer> stack = new Stack<>();
        int maxArea = 0;
        int n = heights.length;
        for (int i = 0; i <= n; i++) {
            int height = i == n ? 0 : heights[i];
            while (!stack.isEmpty() && height < heights[stack.peek()]) {
                int h = heights[stack.pop()];
                int w = stack.isEmpty() ? i : i - stack.peek() - 1;
                maxArea = Math.max(maxArea, h * w);
            }
            stack.push(i);
        }
        return maxArea;
    }

    /**
     * Brute force.
     */ 
    public int largestRectangleArea2(int[] heights) {
        int ans = 0;
        for (int i = 0; i < heights.length; i++) {
            if (heights[i] * (heights.length - i) <= ans) continue;
            int area = heights[i], height = heights[i];
            ans = Math.max(ans, area);
            for (int j = i + 1; j < heights.length; j++) {
                if (area + height * (heights.length - j) <= ans) break;
                if (heights[j] >= height) {
                    area += height;
                } else {
                    area = heights[j] * (j - i + 1);
                    height = heights[j];
                }
                ans = Math.max(ans, area);
            }
        }
        return ans;
    }

    /**
     * Monotonic stack
     */
    public int largestRectangleArea3(int[] heights) {
        int ans = 0;
        
        return ans;
    }
}
