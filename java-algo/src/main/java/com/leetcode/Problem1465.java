package com.leetcode;

import java.util.Arrays;

/**
 * 1465. Maximum Area of a Piece of Cake After Horizontal and Vertical Cuts
 * https://leetcode.com/problems/maximum-area-of-a-piece-of-cake-after-horizontal-and-vertical-cuts/
 */
public class Problem1465 {
    public int maxArea(int h, int w, int[] horizontalCuts, int[] verticalCuts) {
        Arrays.sort(horizontalCuts);
        Arrays.sort(verticalCuts);
        int maxH = findMax(horizontalCuts, h);
        int maxV = findMax(verticalCuts, w);
        int base = (int) (1e9) + 7;
        return (int) ((long) (maxH % base) * (long) (maxV % base) % base);
    }

    private int findMax(int[] arr, int limit) {
        int max = 0;
        for (int i = 0, pre = 0; i <= arr.length; i++) {
            int x = (i == arr.length ? limit : arr[i]) - pre;
            max = Math.max(max, x);
            if (i == arr.length) break;
            pre = arr[i];
        }
        return max;
    }
}
