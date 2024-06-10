package com.leetcode;

import java.util.Arrays;

/**
 * 1051. Height Checker
 * https://leetcode.com/problems/height-checker/
 */
public class Problem1051 {
    public int heightChecker(int[] heights) {
        int[] expected = Arrays.copyOf(heights, heights.length);
        Arrays.sort(expected);
        int ans = 0;
        for (int i = 0; i < heights.length; i++) {
            if (heights[i] != expected[i]) {
                ans++;
            }
        }
        return ans;
    }
}
