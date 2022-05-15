package com.leetcode;

/**
 * 812. Largest Triangle Area
 * https://leetcode.com/problems/largest-triangle-area/
 */
public class Problem812 {
    public double largestTriangleArea(int[][] points) {
        double ans = 0;
        int n = points.length;
        for (int i = 0; i < n - 2; i++) {
            for (int j = i + 1; j < n - 1; j++) {
                for (int k = j + 1; k < n; k++) {
                    double tmp = cal(points[j][0] - points[i][0], points[j][1] - points[i][1], points[k][0] - points[i][0], points[k][1] - points[i][1]);
                    if (tmp > ans) {
                        ans = tmp;
                    }
                }
            }
        }
        return ans;
    }

    private double cal(int a, int b, int c, int d) {
        return Math.abs(a * d - b * c) * 0.5;
    }
}
