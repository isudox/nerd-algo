package com.leetcode;

import java.util.Arrays;

/**
 * 1465. Maximum Area of a Piece of Cake After Horizontal and Vertical Cuts
 * https://leetcode.com/problems/maximum-area-of-a-piece-of-cake-after-horizontal-and-vertical-cuts/
 */
public class Problem1465 {
    public int maxArea(int h, int w, int[] horizontalCuts, int[] verticalCuts) {
        int mod = 1000000007;
        int maxHeight = 0;
        int maxWidth = 0;
        Arrays.sort(horizontalCuts);
        Arrays.sort(verticalCuts);
        for (int i = 0, pre = 0; i <= horizontalCuts.length; i++) {
            int cur;
            if (i == horizontalCuts.length) {
                cur = h - pre;
            } else {
                cur = horizontalCuts[i] - pre;
                pre = horizontalCuts[i];
            }
            if (cur > maxHeight) {
                maxHeight = cur;
            }
        }
        for (int i = 0, pre = 0; i <= verticalCuts.length; i++) {
            int cur;
            if (i == verticalCuts.length) {
                cur = w - pre;
            } else {
                cur = verticalCuts[i] - pre;
                pre = verticalCuts[i];
            }
            if (cur > maxWidth) {
                maxWidth = cur;
            }
        }
        long area = (long) (maxHeight % mod) * (long) (maxWidth % mod);
        return (int) (area % mod);
    }
}
