package com.leetcode;

/**
 * 1037. Valid Boomerang
 * https://leetcode.com/problems/valid-boomerang/
 */
public class Problem1037 {
    public boolean isBoomerang(int[][] points) {
        if (points.length != 3) {
            return false;
        }
        int[] a = points[0], b = points[1], c = points[2];
        return (a[0] - b[0]) * (b[1] - c[1]) != (a[1] - b[1]) * (b[0] - c[0]);
    }
}
