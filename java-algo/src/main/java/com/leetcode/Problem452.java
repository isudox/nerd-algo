package com.leetcode;

import java.util.Arrays;
import java.util.Comparator;

/**
 * 452. Minimum Number of Arrows to Burst Balloons
 * https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/
 */
public class Problem452 {
    public int findMinArrowShots(int[][] points) {
        int n = points.length;
        if (n < 2) return n;
        Arrays.sort(points, Comparator.comparingInt(o -> o[1]));
        int ans = 1, x = points[0][1];
        for (int i = 0; i < n - 1; i++) {
            if (x < points[i + 1][0]) {
                x = points[i + 1][1];
                ans++;
            }
        }
        return ans;
    }
}
