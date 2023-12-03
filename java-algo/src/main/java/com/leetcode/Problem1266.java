package com.leetcode;

/**
 * 1266. Minimum Time Visiting All Points
 * https://leetcode.com/problems/minimum-time-visiting-all-points/
 */
public class Problem1266 {
    public int minTimeToVisitAllPoints(int[][] points) {
        int ans = 0;
        int x = points[0][0], y = points[0][1];
        for (int i = 1; i < points.length; i++) {
            ans += Math.max(Math.abs(points[i][0] - x), Math.abs(points[i][1] - y));
            x = points[i][0];
            y = points[i][1];
        }
        return ans;
    }
}
