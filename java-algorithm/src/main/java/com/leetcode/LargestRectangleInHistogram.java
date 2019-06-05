package com.leetcode;

import java.util.Stack;

/**
 * 84. Largest Rectangle in Histogram
 * https://leetcode.com/problems/largest-rectangle-in-histogram/
 *
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
 *
 * Example:
 *
 *
 * Input: [2,1,5,6,2,3]
 * Output: 10
 */
public class LargestRectangleInHistogram {
    public int largestRectangleArea(int[] heights) {
        Stack<Integer> stack = new Stack<>();
        int maxArea = 0;
        int length = heights.length;
        for (int i = 0; i <= length; i++) {
            int curHeight = i == length ? 0 : heights[i];
            while (!stack.isEmpty() && curHeight < heights[stack.peek()]) {
                int h = heights[stack.pop()];
                int w = stack.isEmpty() ? i : i - stack.peek() - 1;
                maxArea = Math.max(maxArea, h * w);
            }
            stack.push(i);
        }
        return maxArea;
    }
}
