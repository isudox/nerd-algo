package com.leetcode;

/**
 * 1401. Circle and Rectangle Overlapping
 * https://leetcode.com/problems/circle-and-rectangle-overlapping
 */
class Problem1401 {
    public boolean checkOverlap(int radius, int xCenter, int yCenter, int x1, int y1, int x2, int y2) {
        // 圆心在矩形内部
        if (x1 <= xCenter && xCenter <= x2 && y1 <= yCenter && yCenter <= y2) {
            return true;
        }
        int[] a = new int[]{x1 - xCenter, y1 - yCenter}, b = new int[]{x2 - xCenter, y1 - yCenter}, c = new int[]{x2 - xCenter, y2 - yCenter}, d = new int[]{x1 - xCenter, y2 - yCenter};
        return check(a, b, radius) || check(b, c, radius) || check(c, d, radius) || check(d, a, radius);
    }

    private boolean check(int[] p0, int[] p1, int r) {
        if (p0[1] == p1[1]) {  // 边平行于 x 轴
            if (Math.abs(p0[1]) > r) {
                return false;
            }
            if ((p0[0] * p0[0] + p0[1] * p0[1] <= r * r) || (p1[0] * p1[0] + p1[1] * p1[1] <= r * r)) {
                return true;
            }
            return (p0[0] <= 0 && 0 <= p1[0]) || (p1[0] <= 0 && 0 <= p0[0]);
        } else if (p0[0] == p1[0]) { // 边平行于 y 轴
            if (Math.abs(p0[0]) > r) {
                return false;
            }
            if ((p0[0] * p0[0] + p0[1] * p0[1] <= r * r) || (p1[0] * p1[0] + p1[1] * p1[1] <= r * r)) {
                return true;
            }
            return (p0[1] <= 0 && 0 <= p1[1]) || (p1[1] <= 0 && 0 <= p0[1]);
        }
        return false;
    }
}
