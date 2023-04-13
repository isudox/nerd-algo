package com.leetcode;

/**
 * 223. Rectangle Area
 * https://leetcode.com/problems/rectangle-area/
 */
public class Problem223 {
    public int computeArea(int ax1, int ay1, int ax2, int ay2,
                           int bx1, int by1, int bx2, int by2) {
        int total = Math.abs((ax1 - ax2) * (ay1 - ay2)) + Math.abs((bx1 - bx2) * (by1 - by2));
        int cx1 = Math.max(ax1, bx1);
        int cx2 = Math.min(ax2, bx2);
        int cy1 = Math.max(ay1, by1);
        int cy2 = Math.min(ay2, by2);
        if (cx1 < cx2 && cy1 < cy2) {
            return total - (cx2 - cx1) * (cy2 - cy1);
        }
        return total;
    }
}
