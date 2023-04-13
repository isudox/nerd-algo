package com.leetcode;

/**
 * 1779. Find Nearest Point That Has the Same X or Y Coordinate
 * https://leetcode.com/problems/find-nearest-point-that-has-the-same-x-or-y-coordinate/
 */
public class Problem1779 {
    public int nearestValidPoint(int x, int y, int[][] points) {
        int dist = Integer.MAX_VALUE;
        int pos = -1;
        for (int i = 0; i < points.length; i++) {
            int a = points[i][0], b = points[i][1];
            if (a == x || b == y) {
                int cur = Math.abs(x - a) + Math.abs(y - b);
                if (cur < dist) {
                    dist = cur;
                    pos = i;
                }
            }
        }
        return pos;
    }
}
